from db import get_habits_list
from datetime import datetime

def calculate_longest_streak(db, habit_name):
    # Defining the calculating of the longest streak for a habit
    cursor = db.cursor()
    cursor.execute("""SELECT checkoff_date FROM trackers
        INNER JOIN habits ON trackers.habit_id = habits.id
        WHERE habits.name = ?
        ORDER BY checkoff_date ASC""", (habit_name,))
    rows = cursor.fetchall()
    # print(f"Fetched rows for habit{"habit_name"}:{rows}")

    if not rows:
        return 0

    dates = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in rows]
    #print(f"Parsed dates for habit{"habit_name"}:{dates}")

    longest_streak = 1
    current_streak = 1

    for i in range(1,len(dates)):
        if (dates[i]-dates[i-1]).days == 1:
            current_streak += 1
            #print(f"Current streak checked off: {current_streak}")
        else:
            longest_streak = max(longest_streak, current_streak)
            #print(f"New longest streak found:{longest_streak}")
            current_streak = 1

        longest_streak = max(longest_streak, current_streak)
        #print(f"Final longest streak:{longest_streak}")
        return longest_streak

        # Calculating the longest streak from all habits

def longest_streak_all_habits(db):
    habits = get_habits_list(db)
    longest_streak = 0
    for habit in habits:
        streak = calculate_longest_streak(db,habit)
        if streak>longest_streak:
            longest_streak = streak
        return longest_streak





