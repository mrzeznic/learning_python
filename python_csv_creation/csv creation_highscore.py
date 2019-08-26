# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:11:18 2019

@author: MRZEZNIC
"""

import csv

with open('highscore.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Names', 'Highscore'])
    filewriter.writerow(['Mel', '8'])
    filewriter.writerow(['Jack', '5'])
    filewriter.writerow(['David', '3'])
    filewriter.writerow(['Peter', '6'])
    filewriter.writerow(['Maria', '5'])
    filewriter.writerow(['Ryan', '9'])


import pandas as pd

file='highscore.csv'
df = pd.read_csv(file)

print(df)
# print max and min value from cvs file
print('Max', df['Highscore'].max())
print('Min', df['Highscore'].min())

