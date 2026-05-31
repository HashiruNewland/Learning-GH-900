import pandas as pd

# 1. Load the dataset
# Replace 'your_file.csv' with the path to your actual file
try:
    df = pd.read_csv("your_file.csv")
    print("File loaded successfully!")
except FileNotFoundError:
    print("Error: The file could not be found.")
    # Creating a dummy DataFrame for demonstration purposes if file doesn't exist
    data = {
        "User_ID": [101, 102, 102, 104, 105],
        "Age": ["25", "31", "31", None, "150"],
        "Join_Date": [
            "2023-01-15",
            "2023-02-20",
            "2023-02-20",
            "2023-03-01",
            "invalid_date",
        ],
        "Salary": [50000, 62000, 62000, 45000, None],
    }
    df = pd.DataFrame(data)

print("\n--- Original Data ---")
print(df)

# ==========================================
# DATA CLEANING STEPS
# ==========================================

# 2. Remove exact duplicate rows
df = df.drop_duplicates()

# 3. Handle Missing Values (NaN)
# Fill missing salaries with the average (mean) salary of the column
if "Salary" in df.columns:
    mean_salary = df["Salary"].mean()
    df["Salary"] = df["Salary"].fillna(mean_salary)

# Drop rows where 'Age' is missing completely
df = df.dropna(subset=["Age"])

# 4. Fix Data Types & Parse Dates
# Convert Age from string/object to numeric
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Convert Join_Date to standard datetime format (invalid dates become NaT)
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")

# 5. Filter Out Outliers or Unrealistic Data
# Let's assume valid ages must be between 0 and 120
df = df[(df["Age"] >= 0) & (df["Age"] <= 120)]

print("\n--- Cleaned Data ---")
print(df)

# 6. Save the cleaned data to a new file
# df.to_csv('cleaned_output.csv', index=False)
