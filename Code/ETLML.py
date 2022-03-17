import pandas as pd
import numpy as np
import h2o
from h2o.automl import H2OAutoML
import requests
from bs4 import BeautifulSoup
import pickle

##########################################################################################################################################
# I don't recomend to read this code, I have also handed in a serie of notebooks with all the code commented and easy to follow
# With this file I aim to condense all the work and make it easier to run the models for future aplications 
# I also like to write all the code in one file to be able to run it from the terminal without using any interface,
##########################################################################################################################################
# FUNCTIONS,
##########################################################################################################################################
def find_price():
    page = requests.get('https://www.dieselogasolina.com/')
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table').find_all('tr')
    p_E10 = table[1].find_all('td')[1].text
    p_SP98 = table[2].find_all('td')[1].text
    return float(p_SP98[:5].replace(',','.')), float(p_E10[:5].replace(',','.'))

def df_trans(dis, con, gt, prices = find_price()): # Where x is a row in our dataframe, datos de https://www.dieselogasolina.com/
    """ This function is aimed to transform the dataframe and create 2 new columns with the consume per unit of distance and the price per unit
    of distance, it would also be easy to include a column with the total price (distance*price/distance). It should be used as:
                                df[new_columns] = df.apply(lambda x: df_trans(x.distance, x.consume,x.speed,prices=[...]), axis=1)
    It requires an argument with the prices of the gas we are using: [price_SP98, price_E10]"""
    #print(gt)
    cpd = con/dis # The consume per distance is the first thing we can calculate as it doesn't require any transformation


    price = dict({'SP98':prices[0], 'E10':prices[1]})

    ppd = price[gt]*cpd # We can already know the price per distance

    return pd.Series({'con_dis':cpd, 'price_dis':ppd})
##########################################################################################################################################
# 0. EXPLORATION AND TRANSFORMATION OF THE DATA, 
##########################################################################################################################################

df = pd.read_csv('../Data/measurements.csv')
df['snow'] = df.specials.apply(lambda x: True if type(x) != float and 'snow' in x else False)
cols_2drop = ['specials', 'refill liters','refill gas']
df.drop(columns=cols_2drop, inplace=True)
df.temp_inside = df.temp_inside.apply(lambda x: float(x.replace(',','.')) if type(x) != float else x)
df.consume = df.consume.apply(lambda x: float(x.replace(',','.')))
df.distance = df.distance.apply(lambda x: float(x.replace(',','.')))
df.rain = df.rain.apply(lambda x: bool(x))
df.sun = df.sun.apply(lambda x: bool(x))
df.AC = df.AC.apply(lambda x: bool(x))
df.temp_inside.fillna(21.5, inplace=True)
df['temp_gradient'] = df.apply(lambda x: x.temp_outside-x.temp_inside, axis=1)
fp = find_price()
df['gas_price'] = df.gas_type.apply(lambda x: fp[0] if x == 'SP98' else fp[1])
df[['con_dis', 'price_dis']] = df.apply(lambda x:df_trans(x.distance,x.consume,x.gas_type), axis=1)

df.to_csv('../Data/cleaned_mes.csv', index=False)

##########################################################################################################################################
# 1. GENERATION OF THE MODEL, 
##########################################################################################################################################
h2o.init()

datos_h2o = h2o.H2OFrame(df)

train_as_df = h2o.as_list(datos_h2o,use_pandas=True)

train = h2o.H2OFrame(train_as_df)

x = train.columns
y = "price_dis"
x.remove(y)

aml = H2OAutoML(max_models=10, seed=1)
aml.train(x=x, y=y, training_frame=train)
with open('model_pkl', 'wb') as files:
    pickle.dump(aml, files)

print(aml.leader)