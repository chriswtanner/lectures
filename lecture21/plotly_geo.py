import plotly.graph_objs as go
import plotly.offline as plot
import plotly.figure_factory as ff
import numpy as np
import pandas as pd

# install geopandas: pip3 install geopandas
# install pyshp: pip3 install pyshp

# (1) BASIC CHOROPLETH EXAMPLE
# ----------------------------
'''
data_frame = pd.read_csv('https://raw.githubusercontent.com/plotly/' \
	+ 'datasets/master/2011_us_ag_exports.csv')

choropleth = go.Choropleth(z = data_frame['total exports'], \
	locations = data_frame['code'], locationmode = 'USA-states')

layout = go.Layout(title = 'Total exports of the US', geo  = \
	{'scope': 'usa', 'projection': {'type': 'albers usa'}})

figure = go.Figure(data=[choropleth], layout=layout)
plot.plot(figure)
'''

# (2) CHANGE COLORS
# -----------------
'''
color_scale = [[0.0, 'Blue'], [0.5, 'White'], [1.0, 'Red']]
# add a new color attributes to the choropleth
choropleth = go.Choropleth(z = data_frame['total exports'], \
	locations = data_frame['code'], locationmode = 'USA-states', \
	colorscale = color_scale, autocolorscale = False)
layout = go.Layout(title = 'Total exports of the US', geo  = \
	{'scope': 'usa', 'projection': {'type': 'albers usa'}})
figure = go.Figure(data=[choropleth], layout=layout)
plot.plot(figure)
'''

# (3) ADDING TEXT LABELS
# ----------------------
'''
text_labels = data_frame['state'].astype(str) + "<br>Total Exports: " + \
	data_frame['total exports'].astype(str)
color_scale = [[0.0, 'White'], [0.5, '#FF5733'], [1.0, '#900C3F']]
# adding text labels attribute
choropleth = go.Choropleth(z = data_frame['total exports'], \
	locations = data_frame['code'], locationmode = 'USA-states', \
	colorscale = color_scale, autocolorscale = False, \
	text = text_labels)
layout = go.Layout(title = 'Total exports of the US', geo  = \
	{'scope': 'usa', 'projection': {'type': 'albers usa'}})
figure = go.Figure(data=[choropleth], layout=layout)
plot.plot(figure)
'''

# (4) SCATTER-GEO EXAMPLE
# -----------------------
'''
data_frame = pd.read_csv('http://raw.githubusercontent.com/plotly/datasets/' \
	+ 'master/2011_february_us_airport_traffic.csv')
scattergeo = go.Scattergeo(lat = data_frame['lat'], lon = data_frame['long'],\
	mode = 'markers', locationmode = 'USA-states')
layout = go.Layout(title = 'Map of US major airports', geo = {'scope': 'usa', \
	'projection': {'type': 'albers usa'}})
figure = go.Figure(data=[scattergeo], layout=layout)
plot.plot(figure)
'''

# (5) SCATTER-GEO (MAKE SIZE OF DOTS MEAN SOMETHING) EXAMPLE
# ------------------------------------------------------
'''
data_frame = pd.read_csv('http://raw.githubusercontent.com/plotly/datasets/' \
	+ 'master/2011_february_us_airport_traffic.csv')
text_labels = data_frame['airport'].astype(str) + "</br>Takeoff/Landings: " \
	+ data_frame['cnt'].astype(str)
scattergeo = go.Scattergeo(lat = data_frame['lat'], lon = data_frame['long'],\
	mode = 'markers', locationmode = 'USA-states', text = text_labels,\
	marker = {'size': data_frame['cnt'] / 100})

layout = go.Layout(title = 'Map of US major airports', geo = {'scope': 'usa', \
	'projection': {'type': 'albers usa'}})
figure = go.Figure(data=[scattergeo], layout=layout)
plot.plot(figure)
'''

# (6) FIPS GEO EXAMPLE
# -----------------
# to use election data, we just need to change our 'fips' and 'values'
# as those are the only two vital pieces of info -- the rest is for layout/design
#data_frame = pd.read_csv('election-context-2018.csv') # ELECTION DATA

df_sample = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/laucnty16.csv')
df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))

# the CSV lists the FIPS in two parts: state + county, so let's concatenate them
df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']

colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]

fips = df_sample['FIPS'].tolist()

values = df_sample['Unemployment Rate (%)'].tolist() # ADJUST FOR ELECTION DATA
endpts = list(np.mgrid[min(values):max(values):16j])

# ADJUST TITLES FOR ELECTION DATA
fig = ff.create_choropleth(
    fips=fips, values=values,
    binning_endpoints=endpts,
    colorscale=colorscale,
    show_state_data=False,
    show_hover=True, centroid_marker={'opacity': 0},
    asp=2.9, title='USA by Unemployment %',
    legend_title='% unemployed'
)
plot.plot(fig)
