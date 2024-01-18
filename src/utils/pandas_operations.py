import json
import pandas as pd
from src.utils.file_operation import FileOperations


class PandasOperations:
    @staticmethod
    def save_csv(file_path, dataframe):
        dataframe.to_csv(file_path, sep=',', encoding='utf-8', index=False)

    @staticmethod
    def save_pickle(file_path, dataframe):
        dataframe.to_pickle(file_path)

    @staticmethod
    def read_csv(file_path, converters=None):
        # TODO: Converter raises EOF error
        FileOperations.check_file_exists(file_path)
        if converters:
            df = pd.read_csv(file_path, converters=converters, sep=',', encoding='utf-8')
        else:
            df = pd.read_csv(file_path, sep=',', encoding='utf-8')
        return df

    @staticmethod
    def read_pickle(file_path):
        # TODO: Pickle is not working as expected
        pd.read_pickle(file_path)

    @staticmethod
    def convert_str_to_list(column):
        processed_column = column.copy()

        for key, item in processed_column.items():
            if type(item) == str:
                processed_column[key] = json.loads(item)
        return processed_column

    @staticmethod
    def insert_sql(conn, table_name, data_df):
        data_df.to_sql(table_name,
                       conn,
                       if_exists='append',
                       index=False)

    @staticmethod
    def select_sql(conn, query):
        return pd.read_sql(query, conn)

    @staticmethod
    def set_printing_options():
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
