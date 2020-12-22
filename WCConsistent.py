#Question being asked: Which countries perform the best when in the semi-finals?

#Load in packages
import pandas as pd

#Load in dataset
cups = pd.read_csv('/Users/ethanmitten/Desktop/Data Analytics/Python Projects/WorldCupDataset/WorldCups.csv')

#Replace Germany FR with Germany to lower confusion
cups['Winner'] = cups['Winner'].replace('Germany FR', 'Germany')
cups['Runners-Up'] = cups['Runners-Up'].replace('Germany FR', 'Germany')
cups['Third'] = cups['Third'].replace('Germany FR', 'Germany')
cups['Fourth'] = cups['Fourth'].replace('Germany FR', 'Germany')

#Look at all of the countries that have placed in top 4
Winner_Values = cups['Winner'].value_counts()
Second_Values = cups['Runners-Up'].value_counts()
Third_Values = cups['Third'].value_counts()
Fourth_Values = cups['Fourth'].value_counts()
print(Winner_Values, Second_Values, Third_Values, Fourth_Values)

#Create dictionary matching Countries to there Weighted Placement Value
consistent_dict = {'Countries': ['Argentina', 'Austria', 'Belgium', 'Brazil', 'Bulgaria', 'Chile', 'Croatia',
                                  'Czechoslovakia', 'England', 'France', 'Germany', 'Hungary', 'Italy',
                                  'Korea', 'Netherlands', 'Poland', 'Portugal', 'SovietUnion', 'Spain', 'Sweden', 
                                  'Turkey', 'Uruguay', 'USA', 'Yugoslavia'], 
                    'Weighted Placement Value': [17, 3, 1, 32, 1, 2, 2, 6, 5, 12, 37, 6, 25, 1, 12, 4, 3, 1, 5, 8,
                                              2, 11, 2, 2]}

#Turn dictionary into dataframe then sort dataframe by highest placement value
consistent_frame = pd.DataFrame.from_dict(consistent_dict)
sorted_placement = consistent_frame.sort_values('Weighted Placement Value', ascending=False)
print(sorted_placement)

#The only conclusion that can be drawn from this finding is that these are the teams that are consistently
#more "clutch" when playing in the final 4 of the World Cup
print("The top 5 most consistent nations in the World Cup are:\n ", sorted_placement.head())
