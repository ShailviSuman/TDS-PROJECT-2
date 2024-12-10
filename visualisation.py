import os
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'C:\Users\shekhar suman\AppData\Local\Temp\09d15022-5de9-4275-92ce-2c3054f093f2_archive.zip.3f2\Netflix_Movies_and_TV_Shows.csv')


# Check and create 'outputs/' directory
if not os.path.exists('outputs'):
    os.makedirs('outputs')


# Plot histogram (replace 'Genre' with your column)
dataset['Genre'].hist()
plt.title('Distribution of Genre')

# Save the figure
plt.savefig('outputs/histogram.png')
plt.show()
