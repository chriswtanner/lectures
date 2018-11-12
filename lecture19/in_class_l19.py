from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
import plotly.io as pio
import plotly
import os
import numpy as np

def main():

    plotly.offline.plot({
        "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
        "layout": go.Layout(title="hello world")
    }, auto_open=False)

if __name__ == '__main__':
    main()
