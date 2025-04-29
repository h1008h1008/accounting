# Merge Tool

A simple GUI tool to merge multiple Excel or CSV files based on a user-selected key column.

This tool helps you quickly merge multiple data files by allowing you to select the key column to merge on, without writing any code.

## Features
- Support merging `.xlsx`, `.xls`, and `.csv` files.
- Automatically detects all available columns from the files.
- Allows the user to input or select the key column name dynamically.
- Merges data based on the selected key column.
- Outputs the merged result into a new `.xlsx` file.
- Clean and simple interface using built-in `tkinter`.

## Requirements
- Python 3.7+
- pandas
- tkinter (usually included by default in standard Python installations)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/h1008h1008/accounting.git
   cd accounting
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python data-aggregate.py
   ```

2. Follow the on-screen instructions:
   - Select multiple `.xlsx` / `.xls` / `.csv` files to merge.
   - Input the key column name (the column used to merge rows across files).
   - Choose where to save the merged output file.

3. Done! The merged Excel file will be saved at your selected location.

## How to Build as an Executable (.exe)

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the `.exe`:
   ```bash
   pyinstaller --onefile --noconsole data-aggregate.py
   ```

3. The output executable will be located inside the `dist/` folder.

4. (Optional) Use UPX to compress the executable and reduce antivirus false positives:
   - Download UPX from [https://upx.github.io/](https://upx.github.io/)
   - Rebuild using:
     ```bash
     pyinstaller --onefile --noconsole --upx-dir "C:\path\to\upx" merge_tool.py
     ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
