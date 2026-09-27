# Import pandas for data processing
import pandas as pd


# Name of the large accident dataset
file_path = "us_accidents/US_Accidents_March23.csv"


# Store weather-related columns that we need
columns_needed = [
    "Weather_Condition",
    "Severity"
]


# Dictionary to store accident count and severity information
weather_data = {}


# Read the large CSV file in smaller chunks
for chunk in pd.read_csv(
    file_path,
    usecols=columns_needed,
    chunksize=500000
):

    # Remove rows where weather information is missing
    chunk = chunk.dropna(subset=["Weather_Condition"])

    # Group the current chunk by weather condition
    grouped = chunk.groupby("Weather_Condition").agg(
        accident_count=("Severity", "count"),
        total_severity=("Severity", "sum")
    )

    # Add the current chunk's results to the overall results
    for weather, row in grouped.iterrows():

        # If this weather condition is seen for the first time
        if weather not in weather_data:

            # Store accident count and total severity
            weather_data[weather] = {
                "accident_count": row["accident_count"],
                "total_severity": row["total_severity"]
            }

        else:

            # Add accident count from this chunk
            weather_data[weather]["accident_count"] += row["accident_count"]

            # Add severity from this chunk
            weather_data[weather]["total_severity"] += row["total_severity"]


# Convert the dictionary into a DataFrame
weather_summary = pd.DataFrame.from_dict(
    weather_data,
    orient="index"
)


# Give the weather condition a proper column name
weather_summary.index.name = "Weather_Condition"


# Convert the index into a normal column
weather_summary = weather_summary.reset_index()


# Calculate average severity for each weather condition
weather_summary["average_severity"] = (
    weather_summary["total_severity"]
    / weather_summary["accident_count"]
)


# Sort weather conditions from highest to lowest accident count
weather_summary = weather_summary.sort_values(
    "accident_count",
    ascending=False
)


# Save the complete weather analysis
weather_summary.to_csv(
    "weather_severity_analysis.csv",
    index=False
)


# Display the top 15 weather conditions
print("\nTop Weather Conditions by Accident Count:")
print(weather_summary.head(15).to_string(index=False))


# Find the weather condition with the highest accident count
top_weather = weather_summary.iloc[0]


# Display the main finding
print("\nHighest Accident Weather Condition:")
print(
    "Weather:",
    top_weather["Weather_Condition"]
)

print(
    "Accidents:",
    int(top_weather["accident_count"])
)


# Display completion message
print("\nWeather analysis completed successfully!")