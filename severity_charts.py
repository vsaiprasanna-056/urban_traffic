# Import pandas for reading CSV files
import pandas as pd

# Import matplotlib for creating charts
import matplotlib.pyplot as plt


# --------------------------------
# 1. Traffic Signal Average Severity
# --------------------------------

# Read the traffic signal analysis file
signal_df = pd.read_csv("traffic_signal_analysis.csv")

# Create a bar chart for average severity
plt.bar(
    signal_df["Traffic_Signal"].astype(str),
    signal_df["average_severity"]
)

# Add chart title
plt.title("Average Accident Severity by Traffic Signal")

# Add x-axis label
plt.xlabel("Traffic Signal")

# Add y-axis label
plt.ylabel("Average Severity")

# Adjust the layout
plt.tight_layout()

# Save the chart
plt.savefig("traffic_signal_average_severity.png")

# Display the chart
plt.show()


# --------------------------------
# 2. Junction Average Severity
# --------------------------------

# Read the junction analysis file
junction_df = pd.read_csv("junction_analysis.csv")

# Create a bar chart for average severity
plt.bar(
    junction_df["Junction"].astype(str),
    junction_df["average_severity"]
)

# Add chart title
plt.title("Average Accident Severity by Junction")

# Add x-axis label
plt.xlabel("Junction")

# Add y-axis label
plt.ylabel("Average Severity")

# Adjust the layout
plt.tight_layout()

# Save the chart
plt.savefig("junction_average_severity.png")

# Display the chart
plt.show()


# Print completion message
print("Average severity charts created successfully!")