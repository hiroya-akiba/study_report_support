import base64 #バイナリデータの形式を変換させるライブラリ
import io #画像・音声用ライブラリ
import plotly.graph_objects as graph_obj
import matplotlib
matplotlib.use('Agg') # バックエンドの指定
import matplotlib.pyplot as plt
import numpy as np
from .data import DataAccessor

"""
プロットするライブラリのモジュール
1. UsePlotly
2. UseMatplotlib
"""

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

    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def onclick(self, event):
        cid = self.fig.canvas.mpl_connect('button_press_event', 
            print('{} click: button={}, x={}, y={}, xdata={}, ydata={}'.format(
            'double' if event.dblclick else 'single', event.button,
            event.x, event.y, event.xdata, event.ydata,
            ))
        )
        plt.show()

    def draw(d):
        da = DataAccessor
        df = da.create_df(d)


    def create_graph(self):
        """
        plt.cla()でグラフを初期化してから(他の部分でmatplotlibを使っていなければ基本的には必要ない)、グラフを描画している。
        """
        x_list = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]
        t_list = [1, 2, 3,  4,  5,  6,  7,   8,   9,   10]
        plt.cla()
        #plt.plot(t_list, x_list, label="x")
        #plt.xlabel('t')
        #plt.ylabel('x')
        self.ax.scatter(t_list, x_list)


    def get_image(self):
        """
        io.BytesIO()でバイナリーデータを扱うための、領域をメモリーに作り、plt.savefig()で、1つ目の関数で作ったグラフをbufferに保存。
        buffer.getvalue()で、bufferの中身を全てimage_pngに代入。
        base64.b64encodeとbase64decodeはimage_pngないのデータを整えている？もしくは、暗号化している？おそらく。
        buffer.close()でバイナリーデータを扱うためのメモリ領域を削除。
        """
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        image_png = buffer.getvalue()
        graph = base64.b64encode(image_png)
        graph = graph.decode('utf-8')
        buffer.close()
        return graph
    

