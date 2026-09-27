# Import pandas for reading the CSV file
import pandas as pd

# Import matplotlib for creating charts
import matplotlib.pyplot as plt


# Read the traffic signal analysis file
df = pd.read_csv("traffic_signal_analysis.csv")


# Create a bar chart using Traffic Signal and accident count
plt.bar(
    df["Traffic_Signal"].astype(str),
    df["accident_count"]
)

# Add chart title
plt.title("Accidents by Traffic Signal")

# Add x-axis label
plt.xlabel("Traffic Signal")

# Add y-axis label
plt.ylabel("Number of Accidents")

# Adjust the chart layout
plt.tight_layout()

# Save the chart
plt.savefig("traffic_signal_accidents.png")

# Display the chart
plt.show()


# Print completion message
print("Traffic signal chart created successfully!")