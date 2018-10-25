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
        pass
            
    def match(self):
        pass
        
    def validate(self):
        pass
        
    def dispose(self):
        pass
    
    def apply(self):
        pass
        
    def checkResults(self):
        return pd.DataFrame()
            
