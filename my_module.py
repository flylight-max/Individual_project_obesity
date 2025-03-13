import pandas as pd
import seaborn as sns
import numpy as np
import itertools
from scipy.stats import mannwhitneyu

class Outliers:
    def __init__(self,df,col_name):
        self.df = df #Define as attributes
        self.col_name = col_name
        self.iqr = None
        self.percentile_75 = None
        self.percentile_25 = None
    def percentiles(self):
        df_nomiss = self.df[~(self.df[self.col_name].isna())]
        self.percentile_75 = np.percentile(df_nomiss[self.col_name], 75)
        self.percentile_25 = np.percentile(df_nomiss[self.col_name], 25)
        self.iqr = self.percentile_75 - self.percentile_25
        return self.iqr
#I removed return self.iqr because it is not necessary
    def outliers_min(self):
        if self.iqr is None:
            self.percentiles()
        return self.percentile_25 - 1.5*self.iqr
    def outliers_max(self):
        if self.iqr is None:
            self.percentiles()
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
    
def multiple_MannWitU(df, col_name, target_col):
    categories = df[target_col].cat.categories
    results = {}
    for g1,g2 in itertools.combinations(categories, 2):
        data1 = df[df[target_col] == g1][col_name]
        data2 = df[df[target_col] == g2][col_name]
        stat, p = mannwhitneyu(data1, data2)
        #Add a Bonferroni correction
        p = p * len(categories) * (len(categories) - 1) / 2
        results[(g1,g2)] = p
    return results

def boxplot_bef_aft(y,hue):
    fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,8))
    sns.boxplot(x="NObeyesdad",y=y,data=train_set_df, hue=hue, ax=ax1)
    ax1.set_title("Before imputing")
    ax1.set_xticklabels(order_classes,rotation=90)
    sns.boxplot(x="NObeyesdad", y=y, data=new_obesity, hue=hue,ax=ax2)
    ax2.set_title("After imputing")
    ax2.set_xticklabels(order_classes,rotation=90)
    plt.xticks(rotation=90)
    plt.show()