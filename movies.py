#Interesting data about movies on streaming platform
#Our data set: https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney
## Which platform has the most movies?
import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt
import math
import numpy as np

df = pd.read_csv('MoviesOnStreamingPlatforms_updated.csv')
df = df.drop(['Unnamed: 0', 'ID'], axis=1)
df = df.filter(items = ['Netflix','Hulu','Prime Video','Disney+'])
df = df.sum()
x = [df.Netflix,df.Hulu,df['Prime Video'],df['Disney+']]
plt.title('The Number of Movies', fontsize = 20)
plt.xlabel('Movies Platform', fontsize = 20)
ax = df.plot.bar(rot = 0 , xlabel = "Movies Platform", color = ['green','yellow','blue','brown'], figsize = (12,8), fontsize = 16)
for p in ax.patches:
    ax.annotate(str(np.round(p.get_height(),decimals=2)), (p.get_x()+p.get_width()/2.75, p.get_height()),va = 'center', xytext=(0, 10),textcoords='offset points' )


## What does the distribution of IMDb ratings look like?
import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt
import math
import numpy as np
x = ['Netflix','Hulu', 'Prime Video', 'Disney+']
df = pd.read_csv('MoviesOnStreamingPlatforms_updated.csv')
df = df.drop(['Unnamed: 0', 'ID'], axis=1)
data1 = df.filter(items = ['IMDb','Netflix'])
data1 = data1[data1.Netflix == 1]
avgnet = data1.mean()
data2 = df.filter(items = ['IMDb','Hulu'])
data2 = data2[data2.Hulu == 1]
avghulu = data2.mean()
data3 = df.filter(items = ['IMDb','Prime Video'])
data3 = data3[data3['Prime Video'] == 1]
avgprime = data3.mean()
data4 = df.filter(items = ['IMDb','Disney+'])
data4 = data4[data4['Disney+'] == 1]
avgdis = data4.mean()
print(avgnet.IMDb,avghulu.IMDb,avgprime.IMDb,avgdis.IMDb)

import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt
import math
import numpy as np
df = pd.read_csv('MoviesOnStreamingPlatforms_updated.csv')
df = df[df != 'NaN']
df = df.filter(items = ["IMDb"])
plt.figure(figsize=(12, 12), dpi=80)
sbs.displot(data=df, x="IMDb", kde = True)
df.describe()

## What is the distribution of movies’ runtime?
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('MoviesOnStreamingPlatforms_updated.csv')
plt.figure(figsize=(10,6))
plt.title("Movie Length Distribution", fontsize=15)
runtime = df.Runtime
runtime.describe()
runtime = runtime.drop([4405,13179])
plt.title("Movie Length Distribution", fontsize=15)
sns.distplot(runtime)
runtime.describe()

## What is the relationship between movies’ runtime and IMDb ratings?
import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt
import math
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
df = pd.read_csv('MoviesOnStreamingPlatforms_updated.csv')
df = df.drop(['Unnamed: 0', 'ID'], axis=1)
df['Runtimehr'] = df['Runtime']/60
plt.figure(figsize = (15,8))

plt.scatter(df['IMDb'],df['Runtimehr'])
dg = df[['IMDb','Runtimehr']].corr()
print(dg)

## Movies from what year has the highest number on those platforms?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
df = pd.read_csv('MoviesOnStreamingPlatforms_updated.csv')
plt.figure(figsize = (24,10))
df = df.filter(items = ['Year'])
sbs.set_theme(style = "darkgrid")
ax = sns.countplot(x="Year", data=df, palette = "Set1", order=df['Year'].value_counts().index[0:108])
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
df = pd.read_csv('MoviesOnStreamingPlatforms_updated.csv')
plt.figure(figsize = (24,10))
df = df.filter(items = ['Year'])
sbs.set_theme(style = "darkgrid")
ax = sns.countplot(x="Year", data=df, palette = "Set1", order=df['Year'].value_counts().index[0:10])
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=15,
                   xytext = (0, 10), 
                   textcoords = 'offset points')
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.show()

## Is there any relationship between the year the movie was released and IMDb rating?
import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt
import math
df = pd.read_csv('MoviesOnStreamingPlatforms_updated.csv')
df = df.filter(items = ['Year', 'IMDb'])
df = df[df['IMDb'] >= 0]
plt.figure(figsize=(15, 8), dpi=80)

plt.scatter(df['IMDb'],df['Year'])

dg = df[['IMDb','Year']].corr()
print(dg)
## What are the top 10 countries that produced the most movies?
import sidetable
import pandas as pd
import seaborn as sbs
import matplotlib.pyplot as plt
import math
import plotly.express as px

loc_df = {'Lat': [37.0902, 20.5937, 55.3781, 56.1304, -25.2744, 36.2048, 46.2276, 22.3193, 41.8719, 35.9078]
          ,'Long': [-95.7129, 78.9629, -3.4360, -106.3468, 133.7751, 138.2529, 2.2137, 114.1694, 12.5674, 127.7669],
          'color': ['yellow','blue','red','green','pink','purple','orange','brown', 'gold','teal']}
df = pd.read_csv('MoviesOnStreamingPlatforms_updated.csv')
dfreq = df.stb.freq(['Country'])
dcountryList = dfreq[['Country', 'count']]
for i in dcountryList.index:
  index = i
  temp = dcountryList['Country'][i]
  if "," in temp:
    dcountryList.drop([index], inplace= True)
dtop = dcountryList.drop(dcountryList.index[10:len(dcountryList)])
dtop = dtop.reset_index()
dtop = dtop.drop(['index'], axis = 1)
dtop['lat'] = loc_df['Lat']
dtop['long'] = loc_df['Long']
dtop['color'] = loc_df['color']
with open('Yike.txt','r') as f:
  mapbox_key = f.read().strip()
fig = px.scatter_mapbox(dtop, lat="lat", lon = "long", color = "Country",size = "count" ,hover_name="Country",zoom = 1.05)
fig.update_layout(mapbox_style="light", mapbox_accesstoken=mapbox_key)
fig.show()
