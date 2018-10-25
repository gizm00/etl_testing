from database import execute_stored_proc
import pandas as pd

class Etl():
    def __init__(self, data_file, intf_table, match_proc, validate_proc, dispose_proc, apply_proc, results_columns, name):
        self.__data_file = data_file
        self.__intf_table = intf_table
        self.__match_proc = match_proc
        self.__validate_proc = validate_proc
        self.__dispose_proc = dispose_proc        
        self.__apply_proc = apply_proc   
        self.__results_columns = results_columns
        self.__name = name

    def name(self):
        return self.__name

    def initialize(self, db):
        self.__db = db
        
    def loadData(self):
        df_insert = pd.read_csv(self.__data_file, keep_default_na=False)     
        df_insert = df_insert.drop(self.__results_columns, axis=1)
        df_insert.to_sql(
            self.__intf_table.split('.')[1],
            con=self.__db.engine, 
            schema=self.__intf_table.split('.')[0],
            if_exists='append',
            index=False)
            
    def match(self):
        execute_stored_proc('SELECT ' + self.__match_proc, self.__db.conn)
        
    def validate(self):
        execute_stored_proc('SELECT ' + self.__validate_proc, self.__db.conn)
        
    def dispose(self):
        execute_stored_proc('SELECT ' + self.__dispose_proc, self.__db.conn)
    
    def apply(self):
        execute_stored_proc('SELECT ' + self.__apply_proc, self.__db.conn)
        
    def checkResults(self):
        # get just the results columns from both the ETL result and expected result data
        df_result = pd.read_sql('SELECT * FROM ' + self.__intf_table)
        df_result.drop([ col for col in df_result.columns if col not in self.__results_columns ], axis=1)
        df_expected = pd.read_csv(self.__data_file, keep_default_na=False)     
        df_expected = df_insert.drop([ col for col in df_expected.columns if col not in self.__results_columns ], axis=1)
        
        # ensure the columns are in the same order in both data frames
        df_result = df_result.reindex(sorted(df_result.columns), axis=1)
        df_expected = df_expected.reindex(sorted(df_expected.columns), axis=1)

        # ensure data is of the same type between data frames since one is loaded from a file
        # and the other is loaded from the database
        if any(df_result.dtypes != df_expected.dtypes):
            df_result = df_result.astype(df_expected.dtypes)
            
        if df_result.equals(df_expected):
            return pd.DataFrame()
        #else:
            # generate a data frame with the expected and actual results for each row
            # return this to be used for debugging the failures
            
