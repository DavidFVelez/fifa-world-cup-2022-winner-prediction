# -*- coding: utf-8 -*-
"""
  proyecto-data-science-2022-fifa-world-cup

"""

import pandas as pd
from string import ascii_uppercase as alfabeto
import pickle

#Extracción de grupos
tables = pd.read_html('https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')

dict_grupos = {}
for letra, i in zip(alfabeto, range(12, 68, 7)):
  #print(i)
  df = tables[i]
  df.rename(columns={df.columns[1]: 'Team'}, inplace= True)
  df.set_index('Pos', inplace=True)
  df.pop('Qualification')
  dict_grupos[f'Grupo {letra}'] = df
#dict_grupos.keys()
dict_grupos['Grupo A']

#Exportar el diccionario
with open('dict_grupos', 'wb') as output:
  pickle.dump(dict_grupos, output)

from bs4 import BeautifulSoup
import requests

#Extraccion de informacion de los partidos jugados en mundiales anteriores
years = [1930, 1934, 1938, 1942, 1946, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]


def get_games(year):
  page = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
  response = requests.get(page)
  content = response.text
  soup = BeautifulSoup(content, 'lxml')

  #Se genera una lista de todos los partidos con find_all
  games = soup.find_all('div', class_='footballbox')

  #Extraer información importante como anotaciones
  home = []
  score = []
  away = []
  for game in games:
    home.append(game.find('th', class_='fhome').get_text())
    score.append(game.find('th', class_='fscore').get_text())
    away.append(game.find('th', class_='faway').get_text())
    #print(f'{home} {score} {away}')

  dict_matches = {'home' : home, 'score': score, 'away' : away}

  df_matches = pd.DataFrame(dict_matches)
  df_matches['year'] = year
  return df_matches


# record of fifa world cup matches
fifa = [get_games(year) for year in years]

df_cups = pd.concat(fifa, ignore_index= True)

df_cups.to_csv('fifa_cups.csv', index = False)