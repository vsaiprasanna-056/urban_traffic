# Import pandas for reading and working with CSV files
import pandas as pd

# Import matplotlib for creating charts
import matplotlib.pyplot as plt


# -------------------------------
# 1. Accidents by Hour
# -------------------------------

# Read the accident hourly summary file
hour_df = pd.read_csv("accident_hour_summary.csv")

# Create a bar chart using hour and accident count
plt.bar(hour_df["hour"], hour_df["accident_count"])

# Add chart title
plt.title("Accidents by Hour")

# Add label to x-axis
plt.xlabel("Hour of Day")

# Add label to y-axis
plt.ylabel("Number of Accidents")

# Display all hours from 0 to 23
plt.xticks(range(24))

# Adjust the layout
plt.tight_layout()

# Save the chart
plt.savefig("accidents_by_hour.png")

# Display the chart
plt.show()


# -------------------------------
# 2. Accidents by Day
# -------------------------------

# Read the daily accident summary
day_df = pd.read_csv("accident_day_summary.csv")

# Define the correct order of the days
day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# Convert day_of_week into an ordered categorical column
day_df["day_of_week"] = pd.Categorical(
    day_df["day_of_week"],
    categories=day_order,
    ordered=True
)

# Sort the days in Monday-to-Sunday order
day_df = day_df.sort_values("day_of_week")

# Create the bar chart
plt.bar(day_df["day_of_week"], day_df["accident_count"])

# Add chart title
plt.title("Accidents by Day of Week")

# Add x-axis label
plt.xlabel("Day of Week")

# Add y-axis label
plt.ylabel("Number of Accidents")

# Rotate labels slightly
plt.xticks(rotation=30)

# Adjust the layout
plt.tight_layout()

# Save the chart
plt.savefig("accidents_by_day.png")

# Display the chart
plt.show()


# -------------------------------
# 3. Accidents by Severity
# -------------------------------

# Read the severity summary
severity_df = pd.read_csv("accident_severity_summary.csv")

# Create the severity bar chart
plt.bar(
    severity_df["Severity"].astype(str),
    severity_df["accident_count"]
)

# Add chart title
plt.title("Accidents by Severity")

# Add x-axis label
plt.xlabel("Severity")

# Add y-axis label
plt.ylabel("Number of Accidents")

# Adjust the layout
plt.tight_layout()

# Save the chart
plt.savefig("accidents_by_severity.png")

# Display the chart
plt.show()


# -------------------------------
# 4. Top 10 States
# -------------------------------

# Read the state summary
state_df = pd.read_csv("accident_state_summary.csv")

# Select the top 10 states
top_states = state_df.head(10)

# Create the bar chart
plt.bar(
    top_states["State"],
    top_states["accident_count"]
)

# Add chart title
plt.title("Top 10 States by Accident Count")

# Add x-axis label
plt.xlabel("State")

# Add y-axis label
plt.ylabel("Number of Accidents")

# Adjust the layout
plt.tight_layout()

# Save the chart
plt.savefig("top_10_accident_states.png")

# Display the chart
plt.show()


# -------------------------------
# 5. Top 10 Weather Conditions
# -------------------------------

# Read the weather summary
weather_df = pd.read_csv("accident_weather_summary.csv")

# Select the top 10 weather conditions
top_weather = weather_df.head(10)

# Create the bar chart
plt.bar(
    top_weather["Weather_Condition"],
    top_weather["accident_count"]
)

# Add chart title
plt.title("Top 10 Weather Conditions During Accidents")

# Add x-axis label
plt.xlabel("Weather Condition")

# Add y-axis label
plt.ylabel("Number of Accidents")

# Rotate weather labels so they are readable
plt.xticks(rotation=45, ha="right")

# Adjust the layout
plt.tight_layout()

# Save the chart
plt.savefig("top_10_accident_weather.png")

# Display the chart
plt.show()


# Print completion message
print("All accident charts created successfully!")