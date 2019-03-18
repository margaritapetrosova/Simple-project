import plotly.plotly as py
import plotly.graph_objs as go
labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500,2500,1053,500]

trace = go.Pie(labels=labels, values=values)

py.iplot([trace], filename='homework5')
df2.to_csv('task.csv')