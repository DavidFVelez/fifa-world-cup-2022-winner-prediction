from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

path = r'C:\Users\dvelezc\Downloads\chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

#Extraccion de informacion de los partidos jugados en mundiales anteriores
years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]
def get_games(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    driver.get(web)
    games = driver.find_elements(by='xpath', value='//th[@class="fhome"]/..')

    home = []
    score = []
    away = []

    for match in games:
        home.append(match.find_element(by='xpath', value='./th[1]').text)
        score.append(match.find_element(by='xpath', value='./th[2]').text)
        away.append(match.find_element(by='xpath', value='./th[3]').text)

    print(f'{len(home)} {len(score)} {len(away)}')

    dict_fifa = {'home': home, 'score': score, 'away': away}

    df_cups = pd.DataFrame(dict_fifa)
    df_cups['year'] = year
    time.sleep(2)
    #print(df_cups)
    return df_cups



df_for_year = [get_games(year) for year in years]
df_fifa = pd.concat(df_for_year)
df_fifa.to_csv('fifa_cups.csv', index = False )
driver.quit()