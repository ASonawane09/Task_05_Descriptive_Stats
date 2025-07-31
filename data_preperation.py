import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_csv('syracuse_mbb_2023_24_stats.csv')  # Replace with your dataset filename

# Step 2: Explore dataset
print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Preview:")
print(df.head())
print("\nData types and missing values:")
print(df.info())
print(df.isnull().sum())

# Step 3: Clean data
# Example: Drop rows with missing 'Player_Name' (adjust based on your data)
df = df.dropna(subset=['Player'])

# Fill other missing numeric columns with median or zero
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Step 4: Feature engineering
# Example: Create Total_Points as sum of Goals and Assists (adjust column names)
if 'Goals' in df.columns and 'Assists' in df.columns:
    df['Total_Points'] = df['Goals'] + df['Assists']

# Step 5: Descriptive statistics
print("\nDescriptive statistics:")
print(df.describe())

# Optional visualization: histogram of Goals
if 'Goals' in df.columns:
    plt.hist(df['Goals'], bins=10, edgecolor='black')
    plt.title('Distribution of Goals')
    plt.xlabel('Goals')
    plt.ylabel('Frequency')
    plt.show()

# Step 6: Save cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_dataset.csv'")
