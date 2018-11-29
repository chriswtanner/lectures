import plotly.graph_objs as go
import plotly.offline as plot
import numpy as np
import pandas as pd

# (1) BAR GRAPH EXAMPLE
# -------------------
# constructed from a JSON object (like a dictionary), where our keys are x and y
# and their respective values are lists
'''
data = go.Bar({'x':["Cat","Dog"], 'y' : [4,11]})
fig = go.Figure(data=[data])
plot.plot(fig)
'''

# (2) LET'S ADD A TITLE AND LABELS TO THE GRAPH, as it's
# important to tell your audience what your data means
'''
data = go.Bar({'x':["Cat","Dog"], 'y' : [4,11]})
layout = go.Layout(title="Coolness of Dogs versus Cats", yaxis={"title" : "Coolness"})
fig = go.Figure(data = [data], layout=layout) # now graph has title and labels
plot.plot(fig)
'''

# (3) like Main St. in a typical city, we got multiple bars
# -------------------

small = go.Bar({'x':["Cat","Dog"], 'y' : [3.5,8]}, name = "Small")
large = go.Bar({'x':["Cat","Dog"], 'y' : [7,12]}, name = "Large")
layout = go.Layout(title="Coolness of Dogs versus Cats", yaxis={"title" : "Coolness"})
figure = go.Figure(data=[small,large],layout=layout)
plot.plot(figure)


# (4) LINE PLOT EXAMPLE
# -------------------
'''
student1_ages = np.arange(10, 20)
student1_avg_grades = np.random.uniform(50,100,10)

student2_ages = np.arange(10, 20)
student2_avg_grades = np.random.uniform(50,100,10)

years = [2013, 2014, 2015 ... ]
usa = go.Scatter(
	x = years,
	y = num_usa_travellers,
	mode = 'lines+markers',
	name = 'student1'
)
canada = go.Scatter(
	x = years,
	y = num_canada_travellers,
	mode = 'lines+markers',
	name = 'student2'
)
france = go.Scatter(
	x = years,
	y = num_france_travellers,
	mode = 'lines+markers',
	name = 'student2'
)
data = [usa, canada, france]
plot.plot(data)
'''

# (5) SCATTER PLOT EXAMPLE
# -------------------
'''
data = go.Scatter({'x':[5,11,15,24,30],'y':[7.5,9.5,10.8,11.1,11.2]}, \
	mode="markers", name="Dogs")
data2 = go.Scatter({'x':[6,10,15,20,25],'y':[4.5,5,6,8.4,10.3]}, \
	mode="markers", name = "Cats", marker = \
	dict(size = 50, color = 'rgba(255, 0, 0, .9)'))
layout = go.Layout(title = "Coolness versus Height for Cats and Dogs",
	xaxis = {'title': 'Height (in)'}, yaxis={'title' : 'Coolness'})
fig = go.Figure(data=[data, data2], layout = layout)
plot.plot(fig)
'''


# (6) PANDAS -- SCATTER PLOT EXAMPLE
# ----------------------------------
data_frame = pd.read_csv("data.csv")
data = go.Scatter({'x':data_frame["Happiness Score"], \
	'y': data_frame["Economy (GDP per Capita)"]}, mode="markers")

layout = go.Layout(title = "Happiness versus GDP",
	xaxis = {'title': 'Happiness Score'}, yaxis={'title' : 'GDP per Capita'})
fig = go.Figure(data=[data], layout=layout)
plot.plot(fig)


'''
# IN-CLASS ACTIVITY
# -------------------
# which type of plots would be effective for the following:
Q1: Showing the monetary endowment of each of the eight ivy league universities
Q2: Showing (a) # of students and (b) endowment/#students for the Top 500 universities
Q3: Showing the # of tourists to visit Cuba in 2013 - 2017, specifically, those
	who were tourists from USA, Canada, and France.

num_usa_travellers = [68018, 102849, 140153, 190992, 230193]
num_canadian_travellers = [138819, 150894, 168094, 183985, 202852]
num_french_travellers = [129384, 100383, 130781, 141889, 125990]
years = [2013, 2014, 2015, 2016, 2017]
'''
