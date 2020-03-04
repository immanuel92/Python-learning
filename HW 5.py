import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#b.Load the dataset into Python; display a few records.
data = pd.read_csv("hurricanes.csv", sep="|")
dat = data.dropna(subset=['Central_Pressure_mb','Max_Winds_kt'])
dat["Highest_Category"].replace({"TS":0},inplace=True)

dat.head()
dat.tail(3)
dat.columns
dat.values
dat.dtypes

#c.Create summary tables and appropriate plots for Month,and for Highest_Category.
mont=pd.DataFrame(dat['Month'].value_counts())
mont.columns=['No.of_Hurricanes']
mont.plot.bar()
plt.title('Months that Hurricanes Occur in the US (1851-2007)')
plt.xlabel('Month')
plt.ylabel('Count')
#category
cat=pd.DataFrame(dat['Highest_Category'].value_counts())
cat.columns=['No.of_Hurricanes']
cat.plot.bar()
plt.title('Category of Hurricanes in the US (1851-2007)')
plt.xlabel('Category')
plt.ylabel('Count')

#d.Is there a relationship between Central_Pressure_mb and Max_Winds_kt
plt.scatter(dat.Max_Winds_kt,dat.Central_Pressure_mb)
z = np.polyfit(dat.Max_Winds_kt,dat.Central_Pressure_mb,1)
p = np.poly1d(z)
plt.plot(dat.Max_Winds_kt,p(dat.Max_Winds_kt),"r--")
plt.title('Relationship between Central Pressure and Max Winds')
plt.xlabel('Max.Winds in kt')
plt.ylabel('Central.Pressure in mb')
from scipy.stats import spearmanr
corr = spearmanr(dat.Max_Winds_kt,dat.Central_Pressure_mb)
print(corr)

#e.Is there a relationship between Highest_Category and Central_Pressure_mb?
plt.scatter(dat.Highest_Category,dat.Central_Pressure_mb)
z1 = np.polyfit(dat['Highest_Category'],dat['Central_Pressure_mb'],1)
p1 = np.poly1d(z1)
plt.plot(dat.Highest_Category,p1(dat.Highest_Category),"r--")
plt.title('Relationship between Highest Category and Central Pressure')
plt.xlabel('Max.Winds in kt')
plt.ylabel('Central.Pressure in mb')
corr1 = spearmanr(dat.Highest_Category,dat.Central_Pressure_mb)
print(corr1)

#f.Display a table and visualization of Months.

#g.Parse and summarize the data in States_Affected.

#h.Create a table and a visualization showing the number of storms per year for each category.

#i.Create a table and a visualization showing the number of storms per state for each category.


