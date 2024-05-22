import pandas as pd

# File path to your Excel file
file_path = r'C:\Users\gakob\Downloads\Test Files.xlsx'

# Read Excel file into a DataFrame
df = pd.read_excel(file_path)

# Display the DataFrame (contents of the Excel file)
print(df)
