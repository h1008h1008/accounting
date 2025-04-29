import pandas as pd
from tkinter import Tk, filedialog, simpledialog, messagebox
import os

def merge_files_by_key_column_dynamic():
    # Initialize Tkinter and hide main window
    root = Tk()
    root.withdraw()

    # Step 1: Ask user to select multiple files
    file_paths = filedialog.askopenfilenames(
        title="Select files to merge",
        filetypes=[("Excel files", "*.xlsx *.xls"), ("CSV files", "*.csv"), ("All files", "*.*")]
    )

    if not file_paths:
        print("No files selected. Exiting program.")
        return

    all_data = []
    all_columns = set()

    # Step 2: Read all selected files first
    for file_path in file_paths:
        ext = os.path.splitext(file_path)[1].lower()
        try:
            if ext in ['.xlsx', '.xls']:
                df = pd.read_excel(file_path)
            elif ext == '.csv':
                df = pd.read_csv(file_path)
            else:
                print(f"Skipping unsupported file: {file_path}")
                continue

            df.columns = [col.strip() for col in df.columns]  # Clean column names

            all_data.append(df)
            all_columns.update(df.columns)  # Collect all available columns

        except Exception as e:
            print(f"Failed to read {file_path}. Error: {e}")

    if not all_data:
        print("No valid file content found. Exiting program.")
        return

    # Step 3: Keep asking until correct key column is input
    key_column = None
    while True:
        key_column = simpledialog.askstring(
            "Key Column Input",
            f"Available columns:\n{sorted(all_columns)}\n\nPlease enter the key column name:"
        )

        if key_column is None:
            print("No key column entered. Exiting program.")
            return

        key_column = key_column.strip()

        if key_column in all_columns:
            break  # Correct input, exit loop
        else:
            messagebox.showerror("Error", f"The key column '{key_column}' does not exist. Please try again.")

    # Step 4: Merge all data into one DataFrame
    merged_df = pd.concat(all_data, ignore_index=True)

    # Fill NaN with empty string for safe merging
    merged_df = merged_df.fillna('')

    # Define function to merge multiple values into one cell
    def join_values(series):
        series = series.astype(str).str.strip()
        series = series[series != '']
        unique_vals = series.unique()
        return ', '.join(unique_vals) if len(unique_vals) > 0 else ''

    # Group by the key column
    merged_single_row = merged_df.groupby(key_column, dropna=False).agg(join_values).reset_index()

    # Step 5: Ask user where to save the merged file
    save_path = filedialog.asksaveasfilename(
        title="Save merged file",
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")]
    )

    if save_path:
        merged_single_row.to_excel(save_path, index=False)
        print(f"Merging complete! File saved to: {save_path}")
    else:
        print("No save location selected. Exiting program.")

if __name__ == "__main__":
    merge_files_by_key_column_dynamic()
