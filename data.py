import pandas as pd
from datetime import datetime, timedelta
from .query import Query

class DataAccessor:

    def __init__(self):
        pass

    def create_df(d):
        # X軸に設定する日付
        day_list = []
        for i in range(0, d):
            day_list.append(datetime.now().date() - timedelta(days=i))

        # 描画される科目を選別
        reports = Query().get_report(d) # 引数の日付以内の日付のレポートを取得するクエリにしたい
        col = list(reports.values_list("subject__subject_name", flat=True).distinct())
        global_li = [[0 for i in range(len(day_list))] for j in range(len(col))]
        for report in reports:
            report_date = (report.create_time + timedelta(hours=9)).date()               # レポートの作成日時を取得
            date_index = day_list.index(report_date) if report_date in day_list else -1  # 合致するインデックス番号を取得
            if date_index < 0 : continue                                                 # 指定した日時内のレポート以外の場合は載せない
            report_sub = report.subject.subject_name                                     # 科目名を取得
            col_index = col.index(report_sub) if report_sub in col else -1               # 合致するインデックス番号を取得
            global_li[col_index][date_index] += report.time

        # データフレームのdataに代入する辞書を作成
        col_dic = {f"{col[i]}": global_li[i] for i in range(len(col))}

        # データフレームを作成
        return pd.DataFrame(
            data=col_dic,
            index=day_list,
            columns=col)