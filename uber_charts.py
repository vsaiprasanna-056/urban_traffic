# Import pandas to read the Uber summary CSV file.
import pandas as pd

# Import matplotlib to create charts.
import matplotlib.pyplot as plt


# Read the Uber summary CSV file that we already created.
uber_summary = pd.read_csv("uber_summary.csv")


# Display the exact column names in the summary file.
print("Columns in Uber summary:")

# Print all column names.
print(uber_summary.columns.tolist())


# ============================================================
# 1. UBER PEAK HOUR BY DATASET
# ============================================================

# Create a new chart.
plt.figure(figsize=(10, 5))

# Create a bar chart using the file column and peak hour column.
plt.bar(
    uber_summary["file"],
    uber_summary["peak_hour"]
)

# Add a title to the chart.
plt.title("Uber Peak Traffic Hour by Dataset")

# Add a label to the X-axis.
plt.xlabel("Uber Dataset")

# Add a label to the Y-axis.
plt.ylabel("Peak Hour")

# Rotate the dataset names so they are easier to read.
plt.xticks(rotation=45, ha="right")

# Adjust the spacing of the chart.
plt.tight_layout()

# Save the chart as an image.
plt.savefig("uber_peak_hour.png")

# Display the chart.
plt.show()


# ============================================================
# 2. UBER PICKUP VOLUME BY DATASET
# ============================================================

# Take the second column from the summary file.
# In your output, this column contains the number of pickups.
pickup_column = uber_summary.columns[1]

# Create a new chart.
plt.figure(figsize=(10, 5))

# Create a bar chart using the dataset names and pickup counts.
plt.bar(
    uber_summary["file"],
    uber_summary[pickup_column]
)

# Add a title to the chart.
plt.title("Uber Pickup Volume by Dataset")

# Add a label to the X-axis.
plt.xlabel("Uber Dataset")

# Add a label to the Y-axis.
plt.ylabel("Number of Pickups")

# Rotate the dataset names for better readability.
plt.xticks(rotation=45, ha="right")

# Adjust the spacing of the chart.
plt.tight_layout()

# Save the chart as an image.
plt.savefig("uber_pickup_volume.png")

# Display the chart.
plt.show()


# Print a message after both charts are created.
print("Uber charts created successfully!")