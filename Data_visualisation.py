import plotly.express as px
import pandas as pd

df = pd.read_csv("Data.csv")
fig  = px.scatter(df,x='date',y='cases',color='country',size_max=60)
fig.show()

