# This code is using the pandas library to read multiple sheets from an Excel file named
# "三年级分班成绩单.xlsx" and combine them into a single dataframe named "df_all". It then exports this
# combined dataframe to a new Excel file named "三年级总成绩.xlsx" with a sheet named "总成绩".
import pandas as pd

# Get the sheet names from the Excel file
sheet_names = pd.ExcelFile("三年级分班成绩单.xlsx").sheet_names

# Create an empty dataframe to store the combined data
df_all = pd.DataFrame()

# Iterate through each sheet in the Excel file
for i in sheet_names:
    # Read the sheet from the Excel file
    df = pd.read_excel("三年级分班成绩单.xlsx",sheet_name= i)
    # Append the dataframe to the existing dataframe
    df_all = df_all.append(df)

# Export the combined dataframe to an Excel file
df_all.to_excel("三年级总成绩.xlsx",index=False,sheet_name="总成绩")