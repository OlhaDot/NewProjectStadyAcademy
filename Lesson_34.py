import pandas as pd
import numpy as np

from plotly.subplots import make_subplots
import plotly.graph_objects as go

import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\User\Desktop\DS\Population.csv',sep=';')
print(data)

# task 2 - 2 grapth on 1 picture

fig = make_subplots(rows=2, cols=1, subplot_titles=("Population vs Area", "Population vs AVG income"))

fig.add_trace(go.Scatter(x=data['area'], y=data['population'],
                         mode='markers',
                         marker=dict(color='blue'),
                         name = 'Population vs Area'
                        #  xaxis_title="Area",
                        #  yaxis_title="Population"),
              ), row=1, col=1)

fig.add_trace(go.Scatter(x=data['avg_income'], y=data['population'],
                         mode='markers',
                         marker=dict(color='red'),
                         name= 'Population vs AVG income'
                        #  xaxis_title="Average Income",
                        #  yaxis_title="Population"),
              ), row=2, col=1)


fig.update_layout( title_text="Side By Side Subplots")
fig.show()