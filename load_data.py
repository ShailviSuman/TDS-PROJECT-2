import pandas as pd

# Replace 'dataset.csv' with the actual path to your dataset in the `data` folder
dataset = pd.read_csv(r'C:\Users\shekhar suman\AppData\Local\Temp\486fb55f-d91a-4481-82f0-8a66cdfb2e12_archive.zip.e12\Netflix_Movies_and_TV_Shows.csv')

print(dataset.head())
