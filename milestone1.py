
from datetime import date
from workout_tracker import (
    load_workouts,
    days_this_week,
    current_streak,
    most_common_exercise
)

workouts = load_workouts("workouts.json")

today = date(2026, 11, 10)

print("Workout days this week:", days_this_week(workouts, today))
print("Current workout streak:", current_streak(workouts, today))
print("Most common exercise:", most_common_exercise(workouts))


# Self-Checks: test the expected results
assert days_this_week(workouts, today) == 2
assert current_streak(workouts, today) == 4
assert most_common_exercise(workouts) == "Push-ups"

print("All self-checks PASS")

