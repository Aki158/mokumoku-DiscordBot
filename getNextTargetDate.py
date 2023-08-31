import datetime


# 今週のtargetWeekの日付を取得する
def getNextTargetDate(targetWeek):
    # 現在の日付を取得する。
    today = datetime.date.today()

    week = ['月','火','水','木','金','土','日']

    # 曜日をint型で取得する
    weekday = today.weekday()
    # dateから指定した曜日までの加算日数を計算する
    addDays = (7 - weekday + week.index(targetWeek)) % 7
    # dateに加算する
    nextTargetDate = today + datetime.timedelta(days=addDays)

    return str(nextTargetDate) + '(' + targetWeek + ')'