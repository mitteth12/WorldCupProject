#Import necessary packages
import pandas as pd

#Load in the proper data
matches = pd.read_csv('/Users/ethanmitten/Desktop/Data Analytics/Python Projects/WorldCupDataset/WorldCupMatches.csv')
players = pd.read_csv('/Users/ethanmitten/Desktop/Data Analytics/Python Projects/WorldCupDataset/WorldCupPlayers.csv')
cups = pd.read_csv('/Users/ethanmitten/Desktop/Data Analytics/Python Projects/WorldCupDataset/WorldCups.csv')

#Get some general information about what is going on with each dataset
print(matches.head(5))
print(matches.info())

print(players.head(5))
print(players.info())

print(cups.head(5))
print(cups.info())

players['player_name'] = players['Player Name']

players.player_name.unique()

