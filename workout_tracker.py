import json
#載入處理 JSON 的工具

from datetime import date, timedelta
from collections import Counter
def load_workouts(path):
#建立讀取運動紀錄的函式

    with open(path, "r", encoding="utf-8") as file:
    #開啟指定的檔案

        return json.load(file)
        #讀取 JSON，轉成 Python Dictionary


def days_this_week(workouts, today):
    monday = today - timedelta(days=today.weekday())
    count = 0

    for day, exercises in workouts.items():
        workout_date = date.fromisoformat(day)

        if monday <= workout_date <= today and exercises:
            count += 1

    return count


def current_streak(workouts, today):
    streak = 0

    while workouts.get(today.isoformat(), []):
        streak += 1
        today -= timedelta(days=1)

    return streak


def most_common_exercise(workouts):
    counts = Counter()

    for exercises in workouts.values():
        counts.update(exercises)

    if not counts:
        return "No workouts yet"

    return counts.most_common(1)[0][0]


