import pandas as pd
import numpy as np

# code goes here
#loading the data
data = pd.read_csv("diabetes.csv")
#checking dataframe info
# print(data.columns)
# print(data.head())
# print(data.info())
#checking values for accuracy
# print(data.describe())
#replace 0 datas with Nan
data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)
#check actual missing data
print(data.info())
print(data.isnull().sum())
print(data[data.isna().any(axis=1)])
# check data types
print(data.dtypes)
print(data.Outcome.unique())
data[["Outcome"]] = data[["Outcome"]].replace("O",0)
data.Outcome = pd.to_numeric(data.Outcome)
