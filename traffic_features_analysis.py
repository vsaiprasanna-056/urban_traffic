# Import pandas for data processing
import pandas as pd


# Path of the large accident dataset
file_path = "us_accidents/US_Accidents_March23.csv"


# Select only the columns required for this analysis
columns_needed = [
    "Traffic_Signal",
    "Junction",
    "Severity"
]


# Dictionary to store traffic signal results
signal_data = {}


# Dictionary to store junction results
junction_data = {}


# Read the large CSV file in chunks
for chunk in pd.read_csv(
    file_path,
    usecols=columns_needed,
    chunksize=500000
):

    # -------------------------------
    # Traffic Signal Analysis
    # -------------------------------

    # Group accidents based on traffic signal
    signal_group = chunk.groupby("Traffic_Signal").agg(
        accident_count=("Severity", "count"),
        total_severity=("Severity", "sum")
    )

    # Add the current chunk results to the overall results
    for signal, row in signal_group.iterrows():

        # If this value is seen for the first time
        if signal not in signal_data:

            # Store accident count and total severity
            signal_data[signal] = {
                "accident_count": row["accident_count"],
                "total_severity": row["total_severity"]
            }

        else:

            # Add accident count from this chunk
            signal_data[signal]["accident_count"] += row["accident_count"]

            # Add severity from this chunk
            signal_data[signal]["total_severity"] += row["total_severity"]


    # -------------------------------
    # Junction Analysis
    # -------------------------------

    # Group accidents based on junction presence
    junction_group = chunk.groupby("Junction").agg(
        accident_count=("Severity", "count"),
        total_severity=("Severity", "sum")
    )

    # Add the current chunk results to the overall results
    for junction, row in junction_group.iterrows():

        # If this value is seen for the first time
        if junction not in junction_data:

            # Store accident count and total severity
            junction_data[junction] = {
                "accident_count": row["accident_count"],
                "total_severity": row["total_severity"]
            }

        else:

            # Add accident count from this chunk
            junction_data[junction]["accident_count"] += row["accident_count"]

            # Add severity from this chunk
            junction_data[junction]["total_severity"] += row["total_severity"]


# --------------------------------
# Create Traffic Signal DataFrame
# --------------------------------

# Convert the signal dictionary into a DataFrame
signal_summary = pd.DataFrame.from_dict(
    signal_data,
    orient="index"
)

# Give the index a meaningful name
signal_summary.index.name = "Traffic_Signal"

# Convert the index into a normal column
signal_summary = signal_summary.reset_index()

# Calculate average severity
signal_summary["average_severity"] = (
    signal_summary["total_severity"]
    / signal_summary["accident_count"]
)

# Sort by accident count
signal_summary = signal_summary.sort_values(
    "accident_count",
    ascending=False
)

# Save traffic signal analysis
signal_summary.to_csv(
    "traffic_signal_analysis.csv",
    index=False
)


# --------------------------------
# Create Junction DataFrame
# --------------------------------

# Convert the junction dictionary into a DataFrame
junction_summary = pd.DataFrame.from_dict(
    junction_data,
    orient="index"
)

# Give the index a meaningful name
junction_summary.index.name = "Junction"

# Convert the index into a normal column
junction_summary = junction_summary.reset_index()

# Calculate average severity
junction_summary["average_severity"] = (
    junction_summary["total_severity"]
    / junction_summary["accident_count"]
)

# Sort by accident count
junction_summary = junction_summary.sort_values(
    "accident_count",
    ascending=False
)

# Save junction analysis
junction_summary.to_csv(
    "junction_analysis.csv",
    index=False
)


# --------------------------------
# Display Results
# --------------------------------

# Display traffic signal results
print("\nTraffic Signal Analysis:")
print(signal_summary.to_string(index=False))


# Display junction results
print("\nJunction Analysis:")
print(junction_summary.to_string(index=False))


# Display completion message
print("\nTraffic signal and junction analysis completed successfully!")