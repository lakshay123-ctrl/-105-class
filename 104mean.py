import csv

with open('data.csv',newline = '') as f :
    reader = csv.reader(f)
    file_data = list(reader)

#sorting data
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

#getting mean
n = len(new_data)
total = 0
for x in new_data:
    total += x

mean = total/n

import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df, x="Population", y="InternetUsers",
	          size="Percentage",color="Country",
                   size_max=60)

fig.update_layout(shapes=[dict(type = 'line',
y0 = 0,y1 = n,
x0 = mean,x1 = mean)])
fig.update_xaxes(rangemode = "normal")                   
fig.show()


print("mean-average "+str(mean))


