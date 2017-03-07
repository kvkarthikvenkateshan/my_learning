# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:53:10 2017

@author: KKV1
"""
import pandas as pd
import numpy as np
energy = pd.read_excel('Energy Indicators.xls', sheetname = 'Energy', header = 15, skip_footer = 38)
energy.drop(['Unnamed: 0','Unnamed: 1'], axis = 1, inplace = True)
energy.rename(columns = {'Unnamed: 2' : 'Country', 'Renewable Electricity Production' : '% Renewable'},inplace = True)
energy.drop(0, axis = 0, inplace = True)
energy.replace('...', np.nan, inplace = True)
con_energy = energy['Energy Supply']
con_energy *=  1000000
energy.fillna(value = np.nan , inplace = True)
countries = {"Republic of Korea": "South Korea",
             "United States of America": "United States",
             "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
             "China, Hong Kong Special Administrative Region": "Hong Kong"}
#for names in energy['Country']:
#    if names in countries:
#        energy['Country'].replace(names,countries.get(names))
#energy.replace((to_replace = {"energy['Country']":{"Republic of Korea": "South Korea","United States of America": "United States","United Kingdom of Great Britain and Northern Ireland": "United Kingdom","China, Hong Kong Special Administrative Region": "Hong Kong"}}))
#energy.replace(to_replace = {"energy['Country']":{"Republic of Korea": "South Korea","United States of America": "United States","United Kingdom of Great Britain and Northern Ireland": "United Kingdom","China, Hong Kong Special Administrative Region": "Hong Kong"}},inplace = True)

energy.replace({"Republic of Korea": "South Korea",
             "United States of America": "United States",
             "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
             "China, Hong Kong Special Administrative Region": "Hong Kong"},inplace = True)