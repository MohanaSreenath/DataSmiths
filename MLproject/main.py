import data_collection as dc

def main():
    # File paths and connection details
    csv_path = 'Dataset.csv'
    excel_path = 'Book1.xlsx'
    excel_sheet = 'Sheet1'
    sql_connection = 'sqlite:///users.db'
    sql_query = 'SELECT * FROM users_data'

    # Select the dataset to process
    selected_data = dc.select_dataset(csv_path, excel_path, excel_sheet, sql_connection, sql_query)

    if selected_data is not None:
        print("Selected Data:")
        print(selected_data)
    else:
        print("No data available to process.")

if __name__ == "__main__":
    main()
