import numpy as np
import pandas as pd

# importing datasets
songmetadata = pd.read_csv("song_data.csv")
# fwf stands for fixed width file
othermetadata = pd.read_fwf('10000.txt')

# name the columns
othermetadata.columns = ['user_id', 'song_id', 'listen_count']

# merging both datasets
song_df = pd.merge(othermetadata, songmetadata.drop_duplicates(['song_id']), on='song_id', how='left')
#write file in a new csv file

song_df.to_csv(r'merged.csv')
print("processing")
song_df.to_csv("millionsong.xlsx")
print('done!!')
