# Import pandas for data analysis.
import pandas as pd


# Store the path of the US Accidents dataset.
file_path = "us_accidents/US_Accidents_March23.csv"


# Select only the columns needed for our traffic project.
use_columns = [
    "ID",
    "Severity",
    "Start_Time",
    "Start_Lat",
    "Start_Lng",
    "Distance(mi)",
    "State",
    "Temperature(F)",
    "Humidity(%)",
    "Visibility(mi)",
    "Wind_Speed(mph)",
    "Precipitation(in)",
    "Weather_Condition",
    "Traffic_Signal",
    "Junction",
    "Sunrise_Sunset"
]


# Create empty lists to store summary results from each chunk.
hour_results = []
day_results = []
severity_results = []
state_results = []
weather_results = []


# Read the large CSV file in chunks of 500,000 rows.
for chunk in pd.read_csv(
    file_path,
    usecols=use_columns,
    chunksize=500000,
    low_memory=False
):

    # Convert accident start time into datetime format.
    chunk["Start_Time"] = pd.to_datetime(
        chunk["Start_Time"],
        errors="coerce"
    )

    # Remove records where the start time is invalid.
    chunk = chunk.dropna(subset=["Start_Time"])

    # Create the accident hour.
    chunk["hour"] = chunk["Start_Time"].dt.hour

    # Create the day of the week.
    chunk["day_of_week"] = chunk["Start_Time"].dt.day_name()


    # Count accidents for each hour in this chunk.
    hour_results.append(
        chunk.groupby("hour").size().reset_index(
            name="accident_count"
        )
    )


    # Count accidents for each day in this chunk.
    day_results.append(
        chunk.groupby("day_of_week").size().reset_index(
            name="accident_count"
        )
    )


    # Count accidents for each severity level in this chunk.
    severity_results.append(
        chunk.groupby("Severity").size().reset_index(
            name="accident_count"
        )
    )


    # Count accidents for each state in this chunk.
    state_results.append(
        chunk.groupby("State").size().reset_index(
            name="accident_count"
        )
    )


    # Count accidents for each weather condition in this chunk.
    weather_results.append(
        chunk.groupby("Weather_Condition").size().reset_index(
            name="accident_count"
        )
    )


# Combine the hourly results from all chunks.
hour_summary = pd.concat(hour_results)

# Add the counts together for each hour.
hour_summary = hour_summary.groupby(
    "hour",
    as_index=False
)["accident_count"].sum()

# Sort hours from 0 to 23.
hour_summary = hour_summary.sort_values("hour")


# Combine the daily results from all chunks.
day_summary = pd.concat(day_results)

# Add the counts together for each day.
day_summary = day_summary.groupby(
    "day_of_week",
    as_index=False
)["accident_count"].sum()


# Combine the severity results from all chunks.
severity_summary = pd.concat(severity_results)

# Add the counts together for each severity level.
severity_summary = severity_summary.groupby(
    "Severity",
    as_index=False
)["accident_count"].sum()

# Sort severity levels from low to high.
severity_summary = severity_summary.sort_values("Severity")


# Combine the state results from all chunks.
state_summary = pd.concat(state_results)

# Add the counts together for each state.
state_summary = state_summary.groupby(
    "State",
    as_index=False
)["accident_count"].sum()

# Sort states from highest to lowest accident count.
state_summary = state_summary.sort_values(
    "accident_count",
    ascending=False
)


# Combine the weather results from all chunks.
weather_summary = pd.concat(weather_results)

# Add the counts together for each weather condition.
weather_summary = weather_summary.groupby(
    "Weather_Condition",
    as_index=False
)["accident_count"].sum()

# Sort weather conditions from highest to lowest.
weather_summary = weather_summary.sort_values(
    "accident_count",
    ascending=False
)


# Save the hourly accident results.
hour_summary.to_csv(
    "accident_hour_summary.csv",
    index=False
)


# Save the daily accident results.
day_summary.to_csv(
    "accident_day_summary.csv",
    index=False
)


# Save the severity results.
severity_summary.to_csv(
    "accident_severity_summary.csv",
    index=False
)


# Save the state results.
state_summary.to_csv(
    "accident_state_summary.csv",
    index=False
)


# Save the weather results.
weather_summary.to_csv(
    "accident_weather_summary.csv",
    index=False
)


# Find the hour with the highest number of accidents.
peak_hour = hour_summary.loc[
    hour_summary["accident_count"].idxmax()
]


# Print the peak accident hour.
print("\nPeak Accident Hour:")
print(
    "Hour:",
    peak_hour["hour"],
    "| Accidents:",
    peak_hour["accident_count"]
)


# Print the accident counts by day.
print("\nAccidents by Day:")
print(day_summary)


# Print the accident counts by severity.
print("\nAccidents by Severity:")
print(severity_summary)


# Print the top 10 states.
print("\nTop 10 States:")
print(state_summary.head(10))


# Print the top 10 weather conditions.
print("\nTop 10 Weather Conditions:")
print(weather_summary.head(10))


# Print a completion message.
print("\nFull accident analysis completed successfully!")