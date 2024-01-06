import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


df = pd.read_csv('epa-sea-level.csv')
x = df['CSIRO Adjusted Sea Level']
y = df['Year']
fig , ax = plt.subplots()
plt.scatter(x, y)
res = linregress(x,y)
x_pred = pd.Series([i for i in range(1880,2050)])
y_pred = res.slope*x_pred + res.intercept
plt.plot(x_pred, y_pred, 'r')
plt.show()