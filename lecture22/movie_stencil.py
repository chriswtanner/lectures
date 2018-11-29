import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot


def create_data(x_values, y_values):
    colors = ['red', 'blue', 'green', 'yellow', 'pink', 'orange', 'brown']
    data = [go.Scatter(x = x_values, y = y_values, mode='markers', marker={'color': colors})]
    return data


def create_frames(df):
    frames = [{'data': create_data(df['1970_imdb'], df['1970_gross'])},
    {'data': create_data(df['1980_imdb'], df['1980_gross'])},
    {'data': create_data(df['1990_imdb'], df['1990_gross'])},
    {'data': create_data(df['2000_imdb'], df['2000_gross'])},
    {'data': create_data(df['2010_imdb'], df['2010_gross'])}]
    return frames

def create_slider_steps():
    step_list = []
    for year in range(1970, 2011, 10):
        slider_step = {
        'label': year,
        'method': 'animate',
        'args': [
            [year],
            {'frame': {'duration': 200, 'redraw': False},
            'mode': 'immediate',
            'transition': {'duration': 0}}],
        }
        step_list.append(slider_step)
    return step_list

def create_layout(max_value):
    steps = create_slider_steps()
    slider = {'steps': steps}
    layout = go.Layout(title="Movie gross vs imdb scores",
    yaxis = {'range': [0, max_value], 'title': 'Gross $$$$'},
    xaxis = {'range': [0, 10], 'title': "IMDB score"}, sliders=[slider],
    updatemenus= [{'buttons': [{'label': 'Animate', 'method': 'animate', 'args': [None]}],
    'showactive': False,
    'type': 'buttons'}])
    return layout



def build_animation(data_frame):
    """
    TODO: write a function that takes in a pandas dataframe
    """
    data = create_data(data_frame['1970_imdb'], data_frame['1970_gross'])
    # what is this USED for?
    max_gross = 200000000
    frames = create_frames(data_frame)
    layout = create_layout(max_gross)
    figure = go.Figure(data=data, layout=layout, frames=frames)
    plot(figure)



def main():
    data_frame = pd.read_csv("movies.csv")
    build_animation(data_frame)
    # Insert code here

if __name__ == "__main__":
    main()
