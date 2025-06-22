# this script reads two CSV files containing employment levels for different areas in 2020 and 2023, compares them, and outputs the results to a new CSV file.
# it was written entirely by CoPilot using the prompt "write a python script that reads two csv files containing employment levels for different areas in 2020 and 2023, compares them, and outputs the results to a new csv file." as a starting point.
# further modifications were made to calculate percentage changes.
# the model was Gemini 2.5 Pro

# a final change was made to use month1 from 2020 (because of the pandemic)

import pandas as pd
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define file paths
file_2020 = os.path.join(script_dir, "10-2020.csv")
file_2023 = os.path.join(script_dir, "10-2023.csv")
output_file = os.path.join(script_dir, "emplvl_comparison.csv")

try:
    # Read the two CSV files
    df_2020 = pd.read_csv(file_2020, dtype={'area_fips': str})
    df_2023 = pd.read_csv(file_2023, dtype={'area_fips': str})

    # Group by 'area_fips' and sum 'month3_emplvl' for each dataframe
    sum_2020 = df_2020.groupby('area_fips')['month1_emplvl'].sum().reset_index()
    sum_2023 = df_2023.groupby('area_fips')['month3_emplvl'].sum().reset_index()

    # Merge the two dataframes on 'area_fips'
    merged_df = pd.merge(sum_2020, sum_2023, on='area_fips', how='outer')

    # Rename the columns
    merged_df.rename(columns={'month1_emplvl': '2020', 'month3_emplvl': '2023'}, inplace=True)

    # Fill NaN values with 0 if any fips code is in one file but not the other
    merged_df.fillna(0, inplace=True)

    # Calculate the difference and percentage change
    merged_df['difference'] = merged_df['2023'] - merged_df['2020']
    merged_df['percentage_of_2023'] = 0.0
    non_zero_mask = merged_df['2023'] != 0
    merged_df.loc[non_zero_mask, 'percentage_of_2023'] = (merged_df.loc[non_zero_mask, 'difference'] / merged_df.loc[non_zero_mask, '2023']) * 100


    # Save the resulting dataframe to a new CSV file
    merged_df.to_csv(output_file, index=False)

    print(f"Successfully created {output_file}")

except FileNotFoundError as e:
    print(f"Error: {e}. Make sure the CSV files are in the same directory as the script.")
except Exception as e:
    print(f"An error occurred: {e}")
