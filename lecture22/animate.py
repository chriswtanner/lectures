import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot

def create_data(x_values, y_values):
    """
    create_data creates a data object for the graph that you want to visualize
    inputs:
    x_values: a list of the x values of the data
    y_values: a list of the y values of the data
    return: a data object for the x and y values passed in
    """
    data = [go.Scatter(x = x_values, y = y_values, mode='markers', marker={'color': 'Blue', 'size': 10})]

    return data

def create_frames(x, y):
    """
    create_frames creates a list of data objects for each of the steps of the animation
    inputs:
    x, a list of x values
    y, a list of y values
    return:
    a list of data objects for each step of your animation
    """
    frames = [{'data': create_data(x[0], y[0])}, {'data': create_data(x[1], y[1])}, {'data': create_data(x[2], y[2])}, {'data': create_data(x[3], y[3])}]
    return frames


def create_layout():
    """
    create_layout generates the layout for your graph
    returns:
    a layout object for your graph
    """
    layout = go.Layout(updatemenus= [{'buttons': [{'label': 'Animate', 'method': 'animate', 'args': [None]}], 'showactive': False, 'type': 'buttons'}])
    return layout


def build_animation():
    """
    build_animation puts together all of the different objects and generates the actual animation
    """
    x = [[1, -1], [1, -1], [-1, 1], [-1, 1]]
    y = [[1, -1], [-1, 1], [-1, 1], [1, -1]]
    data = create_data(x[0], y[0])
    frames = create_frames(x, y)
    layout = create_layout()
    figure = go.Figure(data=data, layout=layout, frames=frames)
    plot(figure)

def main():
    build_animation()

if __name__ == "__main__":
    main()
