import plotly.graph_objects as graph_obj
import plotly.io as pio
import pandas as pd
from datetime import date, datetime, timedelta
from .models import Report, Subject
from .query import Query

def line_charts():
    fig = graph_obj.Figure(
        graph_obj.Scatter(x=[1,2,3], y=[3,5,2]), layout=graph_obj.Layout(width=400, height=400)
    )
    return fig.to_html(include_plotlyjs=False)

def bar(d):
    # X軸に設定する日付
    day_list = []
    for i in range(0, d):
        day_list.append(datetime.now().date() - timedelta(days=i))

    # 科目毎に勉強時間を出す
    reports = Query().get_report(d)
    col = reports.all().values_list("subject").distinct()
    subject = Query().get_subject(col)
    print(col)
    for sub in subject:
        print(sub)
    print("----")
    #df = pd.DataFrame(index=day_list, columns=col)
    #print(df)
    #reports = Report.objects.filter(create_time=date.today())

    for report in reports:
        print(report.subject)
        
        period = datetime.strftime(report.create_time, '%Y-%m-%d')



    fig = graph_obj.Figure(
        graph_obj.Scatter(x=day_list, y=[3,5,2]), layout=graph_obj.Layout(width=1000, height=400)
    )
    return fig.to_html(include_plotlyjs=False)