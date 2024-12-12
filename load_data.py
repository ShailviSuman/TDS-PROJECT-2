import pandas as pd

# Replace 'dataset.csv' with the actual path to your dataset in the `data` folder
dataset = pd.read_csv(r'C:\Users\shekhar suman\AppData\Local\Temp\09d15022-5de9-4275-92ce-2c3054f093f2_archive.zip.3f2\Netflix_Movies_and_TV_Shows.csv')

print(dataset.head())
print("Dataset Info:")
print(dataset.info())

print("Summary Statistics:")
print(dataset.describe())
