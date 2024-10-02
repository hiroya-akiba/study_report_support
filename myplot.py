import plotly.graph_objects as graph_obj
import matplotlib.pyplot as plt
import numpy as np
from .data import DataAccessor

class UsePlotly:

    def __init__(self):
        pass

    def line_charts(self):
        fig = graph_obj.Figure(
            graph_obj.Scatter(x=[1,2,3], y=[3,5,2]), layout=graph_obj.Layout(width=400, height=400)
        )
        return fig.to_html(include_plotlyjs=False)

    def bar(d):
        da = DataAccessor
        df = da.create_df(d)

        data = [graph_obj.Bar(x=df.index, y=df.iloc[:,i], name=df.columns[i])
                 for i in range(len(df.columns))]
        layout = graph_obj.Layout(
            title = graph_obj.layout.Title(text="日ごとの勉強時間"),
            xaxis = graph_obj.layout.XAxis(title="日時"),
            yaxis = graph_obj.layout.YAxis(title="総勉強時間"),
            barmode = "stack",
            width=1000,
            height=400,
            margin = graph_obj.layout.Margin(l=75, r=75, b=75, t=75)
        )
        fig = graph_obj.Figure(data=data, layout=layout)
        return fig.to_html(include_plotlyjs=False)
    

class UseMatplotlib:

    fig, ax = plt.subplots()
    ax.plot(np.random.rand(10))

    def __init__(self) -> None:
        pass

    def onclick(event):
        print('{} click: button={}, x={}, y={}, xdata={}, ydata={}'.format(
        'double' if event.dblclick else 'single', event.button,
         event.x, event.y, event.xdata, event.ydata,
        ))
        cid = fig.canvas.mpl_connect('button_press_event', onclick)
        plt.show()

    def bar(d):
        da = DataAccessor
        df = da.create_df(d)
