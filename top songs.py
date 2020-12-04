import pandas as pd
songmetadata = pd.read_csv(r'song_data.csv')
othersongdata = pd.read_fwf(r'10000.txt')
songmetadata = pd.DataFrame(songmetadata)
othersongdata.columns = ['user_id','song_id','listen_count']

song_df = pd.merge(othersongdata, songmetadata.drop_duplicates(['song_id']), on='song_id', how='left')

song_grouped = song_df.groupby(['title']).agg({"listen_count":"count"})
grouped_sum = song_grouped['listen_count'].sum()

#calculating the percent share of each song in listen count
song_grouped['percentage'] = song_grouped['listen_count'].div(grouped_sum)*100

#sorting the dataset with respect to listen count
song_grouped = song_grouped.sort_values(['listen_count'],ascending = True)
song_df = song_df['listen_count'].astype(float)
popular = song_grouped.sort_values(by = 'listen_count')

#filtering the top ten songs in the dataset
popularsongs = popular[9517:9567]
popularsongs = pd.DataFrame(popularsongs.reset_index())
popularsongs.sort_values('listen_count', ascending = False)
print(popularsongs)