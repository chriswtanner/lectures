import plotly.graph_objs as go
import plotly.offline as plot
import numpy as np
import pandas as pd

def main():

    # BAR GRAPH EXAMPLE

    data = go.Bar({'x':["Cat","Dog"], 'y' : [4,11]})
    layout = go.Layout(title="Coolness of Dogs versus Cats", yaxis={"title" : "Coolness"})
    fig = go.Figure(data = [data], layout=layout) # now graph has title and labels
    plot.plot(fig)

    # GEOGRAPHIC PLOT EXAMPLE
    '''
    data_frame = pd.read_csv('election-context-2018.csv') # ELECTION DATA

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
    '''

if __name__ == "__main__":
	main()
