# use library and save a lot of keystrokes later on
# create plots without needing an account
import plotly.graph_objs as go
import plotly.offline as plot
import numpy as np
import pandas as pd

# (1) BAR GRAPH EXAMPLE
# -------------------
# constructed from a JSON object (like a dictionary), where our keys are x and y
# and their respective values are lists
#data = go.Bar({'x':["Cat","Dog"], 'y' : [4,11]})
#fig = go.Figure(data=[data])
#plot.plot(fig)


# (2) LET'S ADD A TITLE AND LABELS TO THE GRAPH, as it's
# important to tell your audience what your data means
#layout = go.Layout(title="Coolness of Dogs versus Cats", yaxis={"title" : "Coolness"})
#fig = go.Figure(data = [data], layout=layout) # now graph has title and labels
#plot.plot(fig)
'''

# (3) like Main St. in a typical city, we got multiple bars
small = go.Bar({'x':["Cat","Dog"], 'y' : [3.5,8]}, name = "Small")
large = go.Bar({'x':["Cat","Dog"], 'y' : [7,12]}, name = "Large")
figure = go.Figure(data=[small,large],layout=layout)
plot.plot(figure)
'''

# (4) SCATTER PLOT EXAMPLE
# -------------------
'''
data = go.Scatter({'x':[5,11,15,24,30],'y':[7.5,9.5,10.8,11.1,11.2]}, \
	mode="markers", name="Dogs")
data2 = go.Scatter({'x':[6,10,15,20,25],'y':[4.5,5,6,8.4,10.3]}, \
	mode="markers", name = "Cats", marker = \
	dict(size = 20, color = 'rgba(255, 0, 0, .9)'))
layout = go.Layout(title = "Coolness versus Height for Cats and Dogs",
	xaxis = {'title': 'Height (in)'}, yaxis={'title' : 'Coolness'})
fig = go.Figure(data=[data, data2], layout = layout)
plot.plot(fig)
'''

'''
# (5) PANDAS -- SCATTER PLOT EXAMPLE
data_frame = pd.read_csv("data.csv")
data = go.Scatter({'x':data_frame["Happiness Score"], \
	'y': data_frame["Economy (GDP per Capita)"]}, mode="markers")

layout = go.Layout(title = "Happiness versus GDP",
	xaxis = {'title': 'Happiness Score'}, yaxis={'title' : 'GDP per Capita'})
fig = go.Figure(data=[data], layout=layout)
plot.plot(fig)
'''
