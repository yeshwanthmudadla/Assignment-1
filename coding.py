# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 06:36:47 2023

@author: yeshwanth
"""
#importing libraries
import matplotlib.pyplot as plt
import pandas as pd

#read the csv file
data = pd.read_csv('Human capital, employed female (constant 2018 US$).csv')
data = data.drop(columns=['Series Name', 'Series Code',
                 'Country Code'])
data = data.dropna()
data = data.rename(columns={'Country Name': 'Country'})
data = data.drop([0,1,3,7,10,13,14,15,17,19])
print(data)

M = data['Country']

N= data['2010 [YR2010]']


# line plot


def line(): 
   
    """ Defining the function """
   
    year = ['2004','2005','2006', '2007', '2008', '2009', '2010']
    plt.figure(figsize=(10, 5))
    plt.plot(year, data.iloc[0, 1:8], label='ALB')
    plt.plot(year, data.iloc[1, 1:8], label='ARM')
    plt.plot(year, data.iloc[2, 1:8], label='AUT')
    plt.plot(year, data.iloc[3, 1:8], label='BLR')
    plt.plot(year, data.iloc[4, 1:8], label='BHR')
    plt.plot(year, data.iloc[5, 1:8], label='ARG')
#plotting labels and legend
    plt.xlabel('Year')
    plt.ylabel('Human Capital')
    plt.title('Human capital, employed female (constant 2018 US$) from \
          2014 to 2020')
    plt.legend()      
    plt.show()


# bar graph of year 2010

def bar():
    
    """ Defining the function """
    
    plt.figure(figsize=(15, 5))
    plt.bar(M, N, label='Human Capital')
    plt.xlabel('Country', fontsize = 20)
    plt.ylabel('Human capital', fontsize = 18)
    plt.title('Human capital, employed female (constant 2018 US$)')
    plt.legend()
    plt.show()


#https://databank.worldbank.org/source/sustainable-energy-for-all#


data = pd.read_csv('898deba4-f2c4-4d44-85d9-05157381cde1_Data.csv')
data = data.drop(columns=['Series Name', 'Series Code','Country Code'])
data = data.dropna()
data = data.rename(columns={'Country Name': 'Country'})
#data = data.drop(0,8)
print(data.head())


def pie():
    
    """ Defining the function """
    
    colors = ['#DB8366','#E3A793','#E65525','#C05F3F','#AE7967', \
          '#AE9A67','#DDB95D']
    plt.figure(figsize=(20, 10))
    plt.pie(data['2011 [YR2011]'], labels=data['Country'], \
        autopct=('%2.2f%%'), colors= colors, shadow = True, \
            wedgeprops ={"edgecolor" : "black", 'linewidth' : 1})
    plt.title('Renewable energy consumption (TJ) in year 2011')
    plt.legend()
    plt.show()
 

#Function calling
line()
bar()
pie()   
