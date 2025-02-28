import pandas as pd
import numpy as np

class Outliers:
    def __init__(self,df,col_name):
        self.df = df #Define as attributes
        self.col_name = col_name
        self.iqr = None
        self.percentile_75 = None
        self.percentile_25 = None
    def percentiles(self):
        self.percentile_75 = np.percentile(self.df[self.col_name], 75)
        self.percentile_25 = np.percentile(self.df[self.col_name], 25)
        self.iqr = self.percentile_75 - self.percentile_25
#I removed return self.iqr because it is not necessary
    def outliers_min(self):
        if self.iqr is None:
            self.percentiles()
        return self.percentile_25 - 1.5*self.iqr
    def outliers_max(self):
        if self.iqr is None:
            self.percentile()
        return self.percentile_75 + 1.5*self.iqr
    

class my_labelEncoder:
    def __init__(self):
        self.dict_cat = {}
    
    def fit(self,df,col):
        categories = list(df[col].cat.categories)
        for cat in df[col].cat.categories:
            self.dict_cat[cat] = categories.index(cat)
    
    def transform(self,df,col):
        nb_list = df[col].map(self.dict_cat).astype("Int64") 
        #"Int64" (with capital "I") is pandas’ nullable integer type, which allows NaN.
        return nb_list
    
    def reverse_transform(self,df,col):
        reverse_dict = {v: k for k, v in self.dict_cat.items()}
        return df[col].map(reverse_dict)
