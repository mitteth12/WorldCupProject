#The question being answered is: Does playing in your home continent make a difference?

#Load in packages needed
import pandas as pd

#Load in Datasets
cups = pd.read_csv('/Users/ethanmitten/Desktop/Data Analytics/Python Projects/WorldCupDataset/WorldCups.csv')
matches = pd.read_csv('/Users/ethanmitten/Desktop/Data Analytics/Python Projects/WorldCupDataset/WorldCupMatches.csv')

#See some general information and then see how many null values are missing
print(matches.info)
x = matches.isnull().sum()
print(x)

#Shorten data down to only relevant rows
matches_clean = matches[0:852]

#Drop Null Values and Print Output of How Many Null Values Left
matches_clean = matches_clean.dropna()

#Merge Datasets to get the Host Country for each match
merged_mc = pd.merge(matches_clean, cups, on='Year')
merged_mc = merged_mc.drop(merged_mc.columns[[21,22,23,24,25,26,27,28]], axis=1)

#Add new columns that return boolean values based on whether win or lose
merged_mc['Home_Team_Wins'] = merged_mc['Home Team Goals'].gt(merged_mc['Away Team Goals'])
merged_mc['Away_Team_Wins'] = merged_mc['Away Team Goals'].gt(merged_mc['Home Team Goals'])

#Making Columns for Home Team and Away Team Continents
rating = []
for row in merged_mc['Home Team Name']:
    if row == 'France' :    rating.append('Europe')
    elif row == 'England':   rating.append('Europe')
    elif row == 'USA':  rating.append('North_America')
    elif row == 'Poland':  rating.append('Europe')
    elif row == 'Portugal':  rating.append('Europe')
    elif  row == 'Algeria': rating.append("Africa")  
    elif row  == 'Angola': rating.append("Africa")
    elif row  == 'Argentina': rating.append("South_America")
    elif row  == 'Australia': rating.append("Australia")
    elif row  == 'Austria': rating.append("Europe")
    elif row  == 'Belgium': rating.append("Europe")
    elif row  == 'Brazil': rating.append("South_America")
    elif row  == 'Bolivia': rating.append("South_America")
    elif row  == 'Bulgaria': rating.append("Europe")
    elif row  == 'Cameroon': rating.append("Africa")
    elif row  == 'Canada': rating.append("North_America")
    elif row  == 'Chile': rating.append("South_America")
    elif row  == 'China PR': rating.append("Asia")
    elif row  == 'Colombia': rating.append("South_America")
    elif row  == 'Costa Rica': rating.append("North_America")
    elif row  == 'Croatia': rating.append("Europe")
    elif row  == 'Cuba': rating.append("North_America")
    elif row  == 'Czech Republic': rating.append("Europe")
    elif row  == 'Czechoslovakia': rating.append("Europe")
    elif row  == "Cote d'Ivoire": rating.append("Africa")
    elif row  == 'Denmark': rating.append("Europe")
    elif row  == 'Ecuador': rating.append("South_America")
    elif row  == 'German DR': rating.append("Europe")
    elif row  == 'Germany': rating.append("Europe")
    elif row  == 'Germany FR': rating.append("Europe")
    elif row  == 'Ghana': rating.append("Africa")
    elif row  == 'Greece': rating.append("Europe")
    elif row  == 'Haiti': rating.append("North_America")
    elif row  == 'Honduras': rating.append("North_America")
    elif row  == 'Hungary': rating.append("Europe")
    elif row  == 'IR Iran': rating.append("Asia")
    elif row  == 'Iran': rating.append("Asia")
    elif row  == 'Iraq': rating.append("Asia")
    elif row  == 'Italy': rating.append("Europe")
    elif row  == 'Jamaica': rating.append("North_America")
    elif row  == 'Japan': rating.append("Asia")
    elif row  == 'Korea DPR': rating.append("Asia")
    elif row  == 'Korea Republic': rating.append("Asia")
    elif row  == 'Mexico': rating.append("North_America")
    elif row  == 'Morocco': rating.append("Africa")
    elif row  == 'Netherlands': rating.append("Europe")
    elif row  == 'New Zealand': rating.append("Australia")
    elif row  == 'Nigeria': rating.append("Africa")
    elif row  == 'Northern Ireland': rating.append("Europe")
    elif row  == 'Norway': rating.append("Europe")
    elif row  == 'Paraguay': rating.append("South_America")
    elif row  == 'Peru': rating.append("South_America")
    elif row  == 'Romania': rating.append("Europe")
    elif row  == 'Russia': rating.append("Europe")
    elif row  == 'Saudi Arabia': rating.append("Asia")
    elif row  == 'Scotland': rating.append("Europe")
    elif row  == 'Senegal': rating.append("Africa")
    elif row  == 'Serbia': rating.append("Europe")
    elif row  == 'Slovakia': rating.append("Europe")
    elif row  == 'Slovenia': rating.append("Europe")
    elif row  == 'South Africa': rating.append("Africa")
    elif row  == 'Soviet Union': rating.append("Europe")
    elif row  == 'Spain': rating.append("Europe")
    elif row  == 'Sweden': rating.append("Europe")
    elif row  == 'Switzerland': rating.append("Europe")
    elif row  == 'Togo': rating.append("Africa")
    elif row  == 'Tunisia': rating.append("Africa")
    elif row  == 'Turkey': rating.append("Europe")
    elif row  == 'Ukraine': rating.append("Europe")
    elif row  == 'Uruguay': rating.append("South_America")
    elif row  == 'Wales': rating.append("Europe")
    elif row  == 'Yugoslavia': rating.append("Europe")
    elif row  == 'Zaire': rating.append("Africa")
    else:           rating.append('Not_Rated')
    
merged_mc['Home_Cont'] = rating

ratings = []
for row in merged_mc['Away Team Name']:
    if row == 'France' :    ratings.append('Europe')
    elif row == 'England':   ratings.append('Europe')
    elif row == 'USA':  ratings.append('North_America')
    elif row == 'Poland':  ratings.append('Europe')
    elif row == 'Portugal':  ratings.append('Europe')
    elif  row == 'Algeria': ratings.append("Africa")  
    elif row  == 'Angola': ratings.append("Africa")
    elif row  == 'Argentina': ratings.append("South_America")
    elif row  == 'Australia': ratings.append("Australia")
    elif row  == 'Austria': ratings.append("Europe")
    elif row  == 'Belgium': ratings.append("Europe")
    elif row  == 'Brazil': ratings.append("South_America")
    elif row  == 'Bolivia': ratings.append("South_America")
    elif row  == 'Bulgaria': ratings.append("Europe")
    elif row  == 'Cameroon': ratings.append("Africa")
    elif row  == 'Canada': ratings.append("North_America")
    elif row  == 'Chile': ratings.append("South_America")
    elif row  == 'China PR': ratings.append("Asia")
    elif row  == 'Colombia': ratings.append("South_America")
    elif row  == 'Costa Rica': ratings.append("North_America")
    elif row  == 'Croatia': ratings.append("Europe")
    elif row  == 'Cuba': ratings.append("North_America")
    elif row  == 'Czech Republic': ratings.append("Europe")
    elif row  == 'Czechoslovakia': ratings.append("Europe")
    elif row  == "Cote d'Ivoire": ratings.append("Africa")
    elif row  == 'Denmark': ratings.append("Europe")
    elif row  == 'Ecuador': ratings.append("South_America")
    elif row  == 'German DR': ratings.append("Europe")
    elif row  == 'Germany': ratings.append("Europe")
    elif row  == 'Germany FR': ratings.append("Europe")
    elif row  == 'Ghana': ratings.append("Africa")
    elif row  == 'Greece': ratings.append("Europe")
    elif row  == 'Haiti': ratings.append("North_America")
    elif row  == 'Honduras': ratings.append("North_America")
    elif row  == 'Hungary': ratings.append("Europe")
    elif row  == 'IR Iran': ratings.append("Asia")
    elif row  == 'Iran': ratings.append("Asia")
    elif row  == 'Iraq': ratings.append("Asia")
    elif row  == 'Italy': ratings.append("Europe")
    elif row  == 'Jamaica': ratings.append("North_America")
    elif row  == 'Japan': ratings.append("Asia")
    elif row  == 'Korea DPR': ratings.append("Asia")
    elif row  == 'Korea Republic': ratings.append("Asia")
    elif row  == 'Mexico': ratings.append("North_America")
    elif row  == 'Morocco': ratings.append("Africa")
    elif row  == 'Netherlands': ratings.append("Europe")
    elif row  == 'New Zealand': ratings.append("Australia")
    elif row  == 'Nigeria': ratings.append("Africa")
    elif row  == 'Northern Ireland': ratings.append("Europe")
    elif row  == 'Norway': ratings.append("Europe")
    elif row  == 'Paraguay': ratings.append("South_America")
    elif row  == 'Peru': ratings.append("South_America")
    elif row  == 'Romania': ratings.append("Europe")
    elif row  == 'Russia': ratings.append("Europe")
    elif row  == 'Saudi Arabia': ratings.append("Asia")
    elif row  == 'Scotland': ratings.append("Europe")
    elif row  == 'Senegal': ratings.append("Africa")
    elif row  == 'Serbia': ratings.append("Europe")
    elif row  == 'Slovakia': ratings.append("Europe")
    elif row  == 'Slovenia': ratings.append("Europe")
    elif row  == 'South Africa': ratings.append("Africa")
    elif row  == 'Soviet Union': ratings.append("Europe")
    elif row  == 'Spain': ratings.append("Europe")
    elif row  == 'Sweden': ratings.append("Europe")
    elif row  == 'Switzerland': ratings.append("Europe")
    elif row  == 'Togo': ratings.append("Africa")
    elif row  == 'Tunisia': ratings.append("Africa")
    elif row  == 'Turkey': ratings.append("Europe")
    elif row  == 'Ukraine': ratings.append("Europe")
    elif row  == 'Uruguay': ratings.append("South_America")
    elif row  == 'Wales': ratings.append("Europe")
    elif row  == 'Yugoslavia': ratings.append("Europe")
    elif row  == 'Egypt': ratings.append("Africa")
    elif row  == 'Kuwait': ratings.append("Asia")
    elif row  == 'El Salvador': ratings.append("North_America")
    elif row  == 'Israel': ratings.append("Asia")
    elif row  == 'Dutch West Indies': ratings.append("Asia")
    elif row  == 'Zaire': ratings.append("Africa")
    else:           ratings.append('Not_Rated')
    
merged_mc['Away_Cont'] = ratings


#From this we find True is seen 486 times and False is seen the rest of the time
print(merged_mc['Home_Team_Wins'].describe())

#Make datasets strictly for the winning teams
home_winners = merged_mc[merged_mc['Home_Team_Wins'] == True]
away_winners = merged_mc[merged_mc['Away_Team_Wins'] == True]

#Separate datasets into series for showing outcomes when grouped by Year and Continent
home_year_winners = home_winners.groupby(['Year', 'Home_Cont']).size()
away_year_winners = home_winners.groupby(['Year', 'Away_Cont']).size()

#Concatenate home_year_winners and away_year_winners for easier interpretations in dictionary
merged_winners = pd.concat([home_year_winners, away_year_winners], axis=1)

#Create dictionary for results obtained in merged_winners table
final_piece = {'Year': [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
                        1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014],
               'Host_Country': ['Uruguay', 'Italy', 'France', 'Brazil', 'Switzerland',
                                'Sweden', 'Chile', 'England', 'Mexico', 'Germany',
                                'Argentina', 'Spain', 'Mexico', 'Italy', 'USA',
                                'France', 'Korea/Japan', 'Germany', 'South Africa',
                                'Brazil'],
               'Host_Continent': ['South_America', 'Europe', 'Europe', 'South_America',
                                  'Europe', 'Europe', 'South_America', 'Europe', 'North_America', 
                                  'Europe', 'South_America', 'Europe', 'North_America', 'Europe',
                                  'North_America', 'Europe', 'Asia', 'Europe', 'Africa', 'South_America'],
               'Europe_Wins': [10,28,23,19,37,37,33,40,30,19,36,33,24,32,29,30,27,26,19,25],
               'South_America_Wins': [20,2,4,13,7,9,18,10,15,7,15,10,12,9,8,12,10,11,10,23],
               'North_America_Wins': [6,1,2,6,2,2,3,1,6,2,3,3,3,5,4,3,4,6,3,6],
               'Africa': [0,1,0,0,0,0,0,0,2,1,2,1,1,4,6,6,5,6,4,6],
               'Australia':[0,0,0,0,0,0,0,0,0,1,0,3,0,0,0,0,0,3,2,1],
               'Asia': [0,0,0,0,2,0,0,3,1,0,2,2,2,1,3,5,8,5,7,3]}

#Make a final dataframe that details our findings to the question
final_dataframe = pd.DataFrame.from_dict(final_piece)


#The conclusion that is made is that host country does NOT have an affect on how many wins are gathered
#as Europe has the most wins in every World Cup played












