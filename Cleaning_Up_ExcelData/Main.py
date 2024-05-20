import pandas as pd
import openpyxl

def clean_excel(file_path, sheet_name, column_limits, output_file_path):
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    print("Original Data:")
    print(df.head())


    for column_name, limit in column_limits.items():

        if column_name not in df.columns:
            print(f"Error: Column '{column_name}' does not exist in the Excel sheet.")
            return


        df = df[df[column_name] >= limit]
        print(f"\nAfter filtering '{column_name}' with limit {limit}:")
        print(df.head())


    df.to_excel(output_file_path, index=False)
    print(f"Cleaned data has been saved to '{output_file_path}'.")


# Parameters
file_path = 'C:/First_example/_example.xlsx'
sheet_name = 'Sheet1'  # Change this to your sheet name
column_limits = {  # Change these to your desired column limits
    'ASP': 30,
    'CS': 25,
    'GS': 45,
    'ChemPLP': 40,
    'S(hbond)': 1,
    'S(hb)': 1,
    'S(hbond).2': 1,
    'S(metal)': 1

}
output_file_path = 'C:/First_example/_edited_3.xlsx'

clean_excel(file_path, sheet_name, column_limits, output_file_path)
