# -*- coding: utf-8 -*-
"""Rainfall-prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xWQ8E1FOGhSvMDiGkysYM-YAqHR3dNW7
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv("weatherAUS.csv")
df.head()

df.tail()

df.info()

df.describe()

df.isnull().sum()

df.dtypes

[feature for feature in df.columns if df[feature].dtypes != '0']

numerical_feature = [feature for feature in df.columns if df[feature].dtype != 'object']
[feature for feature in numerical_feature if len(df[feature].unique()<25)]

df.columns

df.isnull().sum()

#null_values
df.isnull().sum()*100/len(df)

numerical_feature

df.head()

df.dtypes

"""Function To Handle Null Values"""

def randomsampleimputation(df, variable):
  df[variable]=df[variable]
  random_sample = df[variable].dropna().sample(df[variable].isnull().sum(),random_state=0)
  random_sample.index = df[df[variable].isnull()].index
  df.loc[df[variable].isnull(),variable] = random_sample

df['RainToday'].isnull().sum()

df['RainToday'].sample(df['RainToday'].isnull().sum(),random_state=0)

numerical_feature = [feature for feature in df.columns if df[feature].dtypes != '0']
discrete_feature = [feature for feature in numerical_feature if len(df[feature].unique())<25]
continuous_feature = [feature for feature in numerical_feature if feature not in discrete_feature]
categorical_feature = [feature for feature in df.columns if feature not in numerical_feature]
print("Numerical feature count".format(len(numerical_feature)))
print("Discrete feature count".format(len(discrete_feature)))
print("Continous feature count".format(len(continuous_feature)))
print("Categorical feature count".format(len(categorical_feature)))

numerical_feature

categorical_feature

df.head()

df.dtypes

df['Cloud3pm'].sample(df['Cloud3pm'].isnull().sum(),random_state=0)

df.head()

for feature in continuous_feature:
  data=df.copy()
  sns.displot(df[feature])
  plt.xlabel(feature)
  plt.ylabel("Count")
  plt.title(feature)
  plt.figure(figsize=(15,15))
  plt.show()

#for continous var handling
for feature in continuous_feature:
  if(df[feature].isnull().sum()>0):
    df[feature] = df[feature].fillna(df[feature].median())

df.isnull().sum()

# for categorical var handling

categorical_feature

df[['Date','Location','WindGustDir','WindDir9am','WindDir3pm','RainToday','RainTomorrow']]

from sklearn import preprocessing
labelencoder = preprocessing.LabelEncoder()

df['Location'] = labelencoder.fit_transform(df['Location'])
df['WindGustDir'] = labelencoder.fit_transform(df['WindGustDir'])
df['WindDir9am'] = labelencoder.fit_transform(df['WindDir9am'])
df['WindDir3pm'] = labelencoder.fit_transform(df['WindDir3pm'])

df[['Date','Location','WindGustDir','WindDir9am','WindDir3pm','RainToday','RainTomorrow']]

df['Date'] = pd.to_datetime(df['Date'],format = "%Y-%m-%d",errors = "coerce")

df[['Date','Location','WindGustDir','WindDir9am','WindDir3pm','RainToday','RainTomorrow']]

df['Date_month'] = df['Date'].dt.month

df.head()

df['Date_day'] = df['Date'].dt.day
df['Date_year'] = df['Date'].dt.year

df.head()

corrmat = df.corr()
plt.figure(figsize=(20,20))
g = sns.heatmap(corrmat, annot=True)

#generate function for outlier

def detect_outliers(df, features):
  for feature in features:
    q1, q3 = df[feature].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    df = df[(df[feature] > lower_bound) & (df[feature] < upper_bound)]
  return df

"""DATA ANALYSIS

"""

import scipy.stats as stats
def qq_plots(df, variable):
  plt.figure(figsize=(15,6))
  plt.subplot(1,2,1)
  df[variable].hist()
  plt.subplot(1,2,2)
  stats.probplot(df[variable], dist="norm", plot=plt)
  plt.show()

for feature in continuous_feature:
  print(feature)
  plt.figure(figsize=(15,6))
  plt.subplot(1,2,1)
  df[feature].hist()
  plt.subplot(1,2,2)
  stats.probplot(df[feature], dist="norm", plot=plt)
  plt.show()

!pip install pandas_profiling

X = df.drop(["RainTomorrow","Date"], axis = 1)
Y = df['RainTomorrow']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.2,random_state=24)

x_train

y_train

y_test
