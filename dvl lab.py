import plotly.express as px
import pandas as pd

# Sample data
data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [5, 4, 3, 2, 1],
    'Z': [2, 3, 4, 1, 5]
}

# Create a DataFrame
df = pd.DataFrame(data)

# 3D Scatter Plot
fig = px.scatter_3d(df, x='X', y='Y', z='Z')
fig.show()