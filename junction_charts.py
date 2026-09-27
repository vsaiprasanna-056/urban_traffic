# Import pandas for reading the CSV file
import pandas as pd

# Import matplotlib for creating charts
import matplotlib.pyplot as plt


# Read the junction analysis file
df = pd.read_csv("junction_analysis.csv")


# Create a bar chart using Junction and accident count
plt.bar(
    df["Junction"].astype(str),
    df["accident_count"]
)

# Add chart title
plt.title("Accidents by Junction")

# Add x-axis label
plt.xlabel("Junction")

# Add y-axis label
plt.ylabel("Number of Accidents")

# Adjust the layout
plt.tight_layout()

# Save the chart
plt.savefig("junction_accidents.png")

# Display the chart
plt.show()


# Print completion message
print("Junction chart created successfully!")