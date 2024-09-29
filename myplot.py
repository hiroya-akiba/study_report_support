import plotly.graph_objects as graph_obj
from datetime import date
from .models import Report, Subject

def line_charts():
    fig = graph_obj.Figure(
        graph_obj.Scatter(x=[1,2,3], y=[3,5,2]), layout=graph_obj.Layout(width=400, height=400)
    )
    return fig.to_html(include_plotlyjs=False)

def bar():
    #model = Report
    # 今日のレポートのみ抽出
    model = Report.objects.filter(create_time=date.today())
    qs = model.order_by("id")[:10]
    #print(model)
    fig = graph_obj.Figure(
        graph_obj.Scatter(x=[1,2,3], y=[3,5,2]), layout=graph_obj.Layout(width=400, height=400)
    )
    return fig.to_html(include_plotlyjs=False)