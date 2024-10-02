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
    reports = Query().get_report(d) # 引数の日付以内の日付のレポートを取得するクエリにしたい
    col = list(reports.values_list("subject__subject_name", flat=True).distinct())

    global_li = [[0] * len(day_list)] * len(col) # 形が同じなのに代入すると下と違うことが分かる。
    # 上記リストは同じリストを複数入れています。そのためひとつのリストの値を変更するだけで、すべてのリストの値が更新されます。
    # それに対し、下記リストでは内包表記で順番に作成された異なるリストが入っているので、実行結果が異なるのです。
    # 引用: トレノキャンプ Pythonの2次元配列の使い方！初期化、追加、検索方法まとめ (https://camp.trainocate.co.jp/magazine/python-two-dimensional-array/)
    global_li = [[0 for i in range(len(day_list))] for j in range(len(col))]
    print([len(v) for v in global_li])
    for report in reports:
        report_date = (report.create_time + timedelta(hours=9)).date() # レポートの作成日時を取得
        date_index = day_list.index(report_date) if report_date in day_list else -1 # 合致するインデックス番号を取得
        if date_index < 0 : continue # 指定した日時内のレポート以外の場合は載せない
        report_sub = report.subject.subject_name # 科目名を取得
        col_index = col.index(report_sub) if report_sub in col else -1 # 合致するインデックス番号を取得
        print(col_index , date_index)
        global_li[col_index][date_index] += report.time

    # データフレームのdataに代入する辞書を作成
    col_dic = {f"{col[i]}": global_li[i] for i in range(len(col))}
    
    # データフレームを作成
    df = pd.DataFrame(
        data=col_dic,
        index=day_list,
        columns=col)

    data = [graph_obj.Bar(x=df.index, y=df.iloc[:,i], name=df.columns[i])
             for i in range(len(col))]
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