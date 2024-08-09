import os
import pandas as pd

def main():
    # Input path for CSV file and result path for JSON file
    csv_file_path = os.getenv('AUV_IN_CSV_FILE_PATH', '')
    json_file_path = os.getenv('AUV_OUT_JSON_FILE_PATH', '')

    # Error file paths
    error_csv_path = os.getenv('AUV_ERR_CSV_ERROR', '')
    error_cleaning_path = os.getenv('AUV_ERR_CSV_ERROR', '')

    try:
        # Read CSV data
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        error_message = f"Error reading CSV data: {e}"
        with open(error_csv_path, 'w') as error_file:
            error_file.write(error_message)
        exit(1)

    try:
        # Do data cleaning

        # Load CSV file into pandas data frame
        df = pd.read_csv(csv_file_path)

        # 1. Convert timestamps
        df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')

        # 2. Change data types
        df['Amount'] = df['Amount'].astype(float)
        mean_item_count = df['ItemCount'].mean()
        df['ItemCount'] = df['ItemCount'].fillna(round(mean_item_count))
        df['ItemCount'] = df['ItemCount'].astype('Int64')

        # 3. Fill missing values
        df['OrderDate'] = df['OrderDate'].fillna(pd.Timestamp.today())
        df['Amount'] = df['Amount'].fillna(df['Amount'].mean())
        df['ItemCount'] = df['ItemCount'].fillna(df['ItemCount'].mean())

        # Export cleaned data as JSON
        df.to_json(json_file_path, orient='records', indent=4)
    except Exception as e:
        error_message = f"Error cleaning the data: {e}"
        with open(error_cleaning_path, 'w') as error_file:
            error_file.write(error_message)
        exit(1)

    print(f"Cleaned data was successfully saved in {json_file_path}.")
    exit(0)

if __name__ == "__main__":
    main()
