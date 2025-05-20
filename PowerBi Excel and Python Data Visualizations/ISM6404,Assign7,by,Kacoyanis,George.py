# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:58:35 2024

@author: gksup
"""
import matplotlib.pyplot as plt
import pandas as pd

d = pd.read_csv(r'C:\Users\gksup\.spyder-py3\ISM6404DataForAssign7.csv')
print(d)

pt1 = pd.pivot_table(d,
values=['Sales'],
index=['Segment'],
aggfunc='sum')
print (pt1)
pt1.plot(kind='bar',figsize=(15,10))
plt.title('Sum of Sales by Segment')
plt.xlabel('Segment')
plt.ylabel('Sum of Sales in USD')
plt.savefig('ISM6404Assign7plt1.jpg')
plt.show()

pt2 = pd.pivot_table(d,
values=['Sales'],
index=['Market'],
aggfunc='sum')
print (pt2)
pt2.plot(kind='bar',figsize=(15,10))
plt.title('Sum of Sales by Market')
plt.xlabel('Market')
plt.ylabel('Sum of Sales in USD')
plt.savefig('ISM6404Assign7plt2.jpg')
plt.show()

pt3 = pd.pivot_table(d,
values=['Sales'],
index=['Category'],
aggfunc='sum')
print (pt3)
pt3.plot(kind='bar',figsize=(15,10))
plt.title('Sum of Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sum of Sales in USD')
plt.savefig('ISM6404Assign7plt3.jpg')
plt.show()

pt4 = pd.pivot_table(d,
values=['Sales'],
index=['Category'],
columns=['Market'],
aggfunc='sum')
print (pt4)
pt4.plot(kind='bar',figsize=(15,10))
plt.title('Sum of Sales by Category and Market')
plt.xlabel('Category')
plt.ylabel('Sum of Sales in USD')
plt.legend(title="Market", loc='best')
plt.savefig('ISM6404Assign7plt4.jpg')
plt.show()

pt5 = pd.pivot_table(d,
values=['Sales'],
index=['Segment'],
columns=['Category'],
aggfunc='sum')
print (pt5)
pt5.plot(kind='bar',figsize=(15,10))
plt.title('Sum of Sales by Segment and Category')
plt.xlabel('Segment')
plt.ylabel('Sum of Sales in USD')
plt.legend(title="Category" , loc='best')
plt.savefig('ISM6404Assign7plt5.jpg')
plt.show()

pt6 = pd.pivot_table(d,
values=['Sales'],
index=['Segment'],
columns=['Category'],
aggfunc='mean')
print (pt6)
pt6.plot(kind='bar',figsize=(15,10))
plt.title('Average Sales by Segment and Category')
plt.xlabel('Segment')
plt.ylabel('Average Sales in USD')
plt.legend(title="Category" , loc='best')
plt.savefig('ISM6404Assign7plt6.jpg')
plt.show()

pt7 = pd.pivot_table(d,
values=['Sales'],
index=['Market'],
columns=['Segment'],
aggfunc='mean')
print (pt7)
pt7.plot(kind='bar',figsize=(15,10))
plt.title('Average Sales by Market and Segment')
plt.xlabel('Market')
plt.ylabel('Average Sales in USD')
plt.legend(title="Segment", loc='best')
plt.savefig('ISM6404Assign7plt7.jpg')
plt.show()

pt8 = pd.pivot_table(d,
values=['Sales'],
index=['Region'], 
columns=['Market'],
aggfunc='sum')
print (pt8)
pt8.plot(kind='bar',figsize=(15,10))
plt.title('Sum of Sales by Region and Market')
plt.xlabel('Region')
plt.ylabel('Sum of Sales in USD')
plt.legend(title="Market", loc='best')
plt.savefig('ISM6404Assign7plt8.jpg')
plt.show()

pt9 = pd.pivot_table(d,
values=['Sales'],
index=['Region'], 
columns=['Segment'],
aggfunc='sum')
print (pt9)
pt9.plot(kind='bar',figsize=(15,10))
plt.title('Sum of Sales by Region and Segment')
plt.xlabel('Region')
plt.ylabel('Sum of Sales in USD')
plt.legend(title="Segment", loc='best')
plt.savefig('ISM6404Assign7plt9.jpg')
plt.show()

pt10 = pd.pivot_table(d,
values=['Sales'],
index=['Region'],
columns=['Segment'],
aggfunc='mean')
print (pt10)
pt10.plot(kind='bar',figsize=(15,10))
plt.title('Average Sales by Region and Segment')
plt.xlabel('Region')
plt.ylabel('Average Sales in USD')
plt.legend(title="Segment", loc='best')
plt.savefig('ISM6404Assign7plt10.jpg')
plt.show()