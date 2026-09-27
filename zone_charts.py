# Import pandas for reading and analysing the CSV file
import pandas as pd

# Import matplotlib for creating the chart
import matplotlib.pyplot as plt


# Read the zone-level congestion results
df = pd.read_csv("zone_congestion_summary.csv")


# Sort zones by trip count so that we can focus on high-volume zones
df = df.sort_values(
    "trip_count",
    ascending=False
)


# Select the top 10 high-volume zones
top_zones = df.head(10).copy()


# Sort the selected zones by average speed
# Lower speed means more congestion
top_zones = top_zones.sort_values(
    "average_speed",
    ascending=True
)


# Create the bar chart
plt.figure(figsize=(10, 6))

# Plot average speed for each zone
plt.bar(
    top_zones["zone"],
    top_zones["average_speed"]
)

# Add chart title
plt.title("Average Speed in Top 10 High-Volume Zones")

# Add x-axis label
plt.xlabel("Pickup Zone")

# Add y-axis label
plt.ylabel("Average Speed (mph)")

# Rotate zone names so they are easy to read
plt.xticks(rotation=45, ha="right")

# Adjust the layout
plt.tight_layout()

# Save the chart
plt.savefig(
    "zone_congestion_chart.png",
    dpi=300
)

# Display the chart
plt.show()

# Print completion message
print("Zone congestion chart created successfully!")
print("Output file: zone_congestion_chart.png")