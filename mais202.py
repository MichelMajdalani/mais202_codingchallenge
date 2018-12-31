# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:10:20 2018

@author: miche
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

#reads csv file and assign it to dataset variable which is located in the same folder as python file
dataset = pd.read_csv("data.csv") 

#prints the two columns of interest: interest rate and purpose
#print(dataset[["int_rate","purpose"]]) 

#use groupby to split data by purposes
purposes = dataset.groupby("purpose")


#for purpose, purpose_df in purposes:
#    print(purpose)
#    print(purpose_df[["int_rate"]])


fdata = purposes.mean()[["int_rate"]]
print(fdata.round(3))

#Plot

#x coordinate as indices 
xpos = np.arange(len(fdata.index))
#y coordinate as list of average interest rate
ypos = fdata["int_rate"].tolist()
#print(fdata.index)

plt.xticks(xpos, fdata.index)
plt.xlabel(fdata.index.name)
plt.ylabel("mean(int_rate)")
plt.bar(xpos,ypos,color=['green','orange','blue','pink', 'red', 'yellow'])
plt.xticks(rotation=65)




    