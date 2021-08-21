import tensorflow as tf
import pandas as pd


data = pd.read_csv('/Users/malachi/Downloads/titanic/train.csv')

print(data['Fare'])
