import pandas as pd

# Read the CSV file into a DataFrame
data_df = pd.read_csv('NSMES1988new.csv')

# Display information about the DataFrame, including the data types of columns before changing
data_df.info()

# List of columns to convert to category data type
changeToCategory = ['gender', 'health', 'adl', 'employed', 'insurance', 'medicaid']

# List of numerical columns to convert to int16 data type
numerical_cols = ['visits', 'nvisits', 'ovisits', 'novisits', 'emergency', 
                  'hospital', 'chronic', 'age', 'school', 'married']

# Convert numerical columns to int16 data type
for col in numerical_cols:
    data_df[col] = data_df[col].astype('int16')

# Convert categorical columns to category data type
for col in changeToCategory:
    data_df[col] = data_df[col].astype('category')

# Drop the 'afam' column
data_df.drop(columns=['afam'], inplace=True)

# Display information about the DataFrame, including the data types of columns
data_df.info()
