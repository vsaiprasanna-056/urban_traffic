# Import pandas to read the summary CSV files.
import pandas as pd

# Import matplotlib to create charts.
import matplotlib.pyplot as plt


# ============================================================
# 1. TAXI TRIPS BY HOUR
# ============================================================

# Read the hourly taxi summary CSV file.
hour_summary = pd.read_csv("taxi_hour_summary.csv")

# Sort the data from hour 0 to hour 23.
hour_summary = hour_summary.sort_values("hour")

# Create a new chart with a suitable size.
plt.figure(figsize=(10, 5))

# Create a line chart showing the number of trips for each hour.
plt.plot(
    hour_summary["hour"],
    hour_summary["trip_count"],
    marker="o"
)

# Add a title to the chart.
plt.title("NYC Taxi Traffic Volume by Hour")

# Add a label to the X-axis.
plt.xlabel("Hour of Day")

# Add a label to the Y-axis.
plt.ylabel("Number of Taxi Trips")

# Show all 24 hours on the X-axis.
plt.xticks(range(24))

# Add grid lines to make the chart easier to understand.
plt.grid(True)

# Automatically adjust the spacing of the chart.
plt.tight_layout()

# Save the chart as an image file.
plt.savefig("taxi_trips_by_hour.png")

# Display the chart.
plt.show()


# ============================================================
# 2. TAXI TRIPS BY DAY OF WEEK
# ============================================================

# Read the daily taxi summary CSV file.
day_summary = pd.read_csv("taxi_day_summary.csv")

# Create a new chart with a suitable size.
plt.figure(figsize=(10, 5))

# Create a bar chart showing taxi trips for each day.
plt.bar(
    day_summary["day_of_week"],
    day_summary["trip_count"]
)

# Add a title to the chart.
plt.title("NYC Taxi Traffic Volume by Day")

# Add a label to the X-axis.
plt.xlabel("Day of Week")

# Add a label to the Y-axis.
plt.ylabel("Number of Taxi Trips")

# Rotate the day names slightly for better readability.
plt.xticks(rotation=30)

# Automatically adjust the chart spacing.
plt.tight_layout()

# Save the chart as an image file.
plt.savefig("taxi_trips_by_day.png")

# Display the chart.
plt.show()


# ============================================================
# 3. WEEKDAY VS WEEKEND
# ============================================================

# Read the weekday/weekend summary CSV file.
day_type_summary = pd.read_csv("taxi_day_type_summary.csv")

# Create a new chart with a suitable size.
plt.figure(figsize=(8, 5))

# Create a bar chart comparing weekday and weekend trips.
plt.bar(
    day_type_summary["day_type"],
    day_type_summary["trip_count"]
)

# Add a title to the chart.
plt.title("NYC Taxi Trips: Weekday vs Weekend")

# Add a label to the X-axis.
plt.xlabel("Day Type")

# Add a label to the Y-axis.
plt.ylabel("Number of Taxi Trips")

# Automatically adjust the chart spacing.
plt.tight_layout()

# Save the chart as an image file.
plt.savefig("taxi_weekday_vs_weekend.png")

# Display the chart.
plt.show()


# ============================================================
# 4. CONGESTION / AVERAGE SPEED BY HOUR
# ============================================================

# Read the taxi congestion summary CSV file.
congestion_summary = pd.read_csv("taxi_congestion_summary.csv")

# Sort the congestion data by hour.
congestion_summary = congestion_summary.sort_values("hour")

# Create a new chart with a suitable size.
plt.figure(figsize=(10, 5))

# Create a line chart showing average taxi speed for each hour.
plt.plot(
    congestion_summary["hour"],
    congestion_summary["avg_speed"],
    marker="o"
)

# Add a title to the chart.
plt.title("NYC Taxi Average Speed by Hour")

# Add a label to the X-axis.
plt.xlabel("Hour of Day")

# Add a label to the Y-axis.
plt.ylabel("Average Speed (mph)")

# Show all 24 hours on the X-axis.
plt.xticks(range(24))

# Add grid lines to the chart.
plt.grid(True)

# Automatically adjust the chart spacing.
plt.tight_layout()

# Save the chart as an image file.
plt.savefig("taxi_average_speed_by_hour.png")

# Display the chart.
plt.show()


# Print a message after all charts are created.
print("All taxi charts created successfully!")