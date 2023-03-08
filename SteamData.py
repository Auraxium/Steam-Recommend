import pandas as pd
import os.path

Data = pd.read_csv(os.getcwd() + '/steam_games.csv', on_bad_lines='skip')
print(len(newData))