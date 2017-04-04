import pandas as pd 
import numpy as np
df = pd.read_csv('City_Zhvi_AllHomes.csv')
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
state_region = ['State','RegionName']
cloumns_to_keep = list(df.columns[51:])
df = df[state_region + cloumns_to_keep]
df.fillna(value = 0, inplace = True)
df = df.dropna()
col = pd.Series(df.columns)
l_q = []
for i in col:
    if (i.endswith('01') or i.endswith('02') or i.endswith('03')):
        y_q = i[:4] + 'q1'
        l_q.append(y_q)
    elif (i.endswith('04') or i.endswith('05') or i.endswith('06')):
        y_q = i[:4] + 'q2'
        l_q.append(y_q)
    elif (i.endswith('07') or i.endswith('08') or i.endswith('09')):
        y_q = i[:4] + 'q3'
        l_q.append(y_q)
    else:
        y_q = i[:4] + 'q4'
        l_q.append(y_q)
df = df.T
df['Quarter'] = l_q
df1 = df.groupby('Quarter').agg(np.mean)
df2 = df1.T