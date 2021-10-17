import pandas as pd
import plotly.graph_objects as pg
df = pd.read_csv('data.csv')
id = input('Please Enter Student ID : ')
studentdf = df.loc[df['student_id'] == id]
newData = studentdf.groupby('level')['attempt'].mean()
graph = pg.Figure(pg.Bar(
    x = ['Level 1', 'Level 2', 'Level 3', 'Level 4'], y = newData
))
graph.show()