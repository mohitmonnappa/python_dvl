import plotly.express as px
import pandas as pd
x = []
y= []
z = []
file = open('9.txt', 'r+')
for lines in file:
    ln = lines.split()
    x.append(ln[0])
    y.append(ln[1])
    z.append(ln[2])
data = {'x':x,'y':y,'z':z}
df = pd.DataFrame(data)
print(df)

fig = px.scatter_3d(df, x='x', y='y', z='z')
fig.show()