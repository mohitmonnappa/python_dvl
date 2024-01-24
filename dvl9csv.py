# Read from CSV file
import plotly.express as px
import pandas as pd

df = pd.read_csv(r'C:\Users\mohit\Downloads\SampleCSVFile_11kb.csv')

# 3D Scatter Plot
fig = px.scatter_3d(df, x='X', y='Y', z='Z')
fig.show()
