import pandas as pd

melbourne_file_path = '/Users/mac/Desktop/MachineLearning/Basic Data Exploration/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
print(melbourne_data.columns)

melbourne_data = melbourne_data.dropna(axis=0)


