from db import get_db
from tracker import Tracker
from datetime import datetime

"""Function for loading the predefined habits and their checkoff dates into database"""
def predefined_habits_db():
    db = get_db
    cursor = db.cursor()
    # Create tables if they do not exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS habits (
                        id INTEGER PRIMARY KEY,
                        name TEXT UNIQUE NOT NULL,
                        periodicity TEXT NOT NULL,
                        start_date TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS trackers (
                        id INTEGER PRIMARY KEY,
                        habit_id INTEGER,
                        checkoff_date TEXT,
                        FOREIGN KEY (habit_id) REFERENCES habits (id)
                    )''')
    db.commit()

    habits = {
        "running": ["2024-12-01", "2024-12-02", "2024-12-03", "2024-12-04", "2024-12-05", "2024-12-06", "2024-12-07",
                  "2024-12-08", "2024-12-09", "2024-12-10", "2024-12-11", "2024-12-12", "2024-12-13", "2024-12-14",
                  "2024-12-15", "2024-12-16", "2024-12-17", "2024-12-18", "2024-12-19", "2024-12-20", "2024-12-21",
                  "2024-12-22", "2024-12-23", "2024-12-24", "2024-12-25", "2024-12-26", "2024-12-27", "2024-12-28",
                  "2024-12-29", "2024-12-30", "2024-12-31"],
        "meditating": ["2024-12-01", "2024-12-03", "2024-12-04", "2024-12-05", "2024-12-06", "2024-12-07", "2024-12-08",
                 "2024-12-09", "2024-12-10", "2024-12-11", "2024-12-12", "2024-12-14", "2024-12-15", "2024-12-16",
                 "2024-12-17", "2024-12-18", "2024-12-19", "2024-12-20", "2024-12-21", "2024-12-22", "2024-12-23",
                 "2024-12-25", "2024-12-26", "2024-12-27", "2024-12-28", "2024-12-29", "2024-12-30", "2024-12-31"],
        "swimming": ["2024-12-01", "2024-12-08", "2024-12-15", "2024-12-23", "2024-12-30"],
        "reading_book": ["2024-12-01", "2024-12-09", "2024-12-16", "2024-12-23", "2024-12-30"],
        "walking_in_nature": ["2024-12-03", "2024-12-10","2024-12-17","2024-12-23","2024-12-30"]
    }

    for habit, dates in habits.items():
        cursor.execute('SELECT id FROM habits WHERE name = ?', (habit,))
        habit_id = cursor.fetchone()
        if not habit_id:
            tracker = Tracker(habit, f"{habit} habit", "Daily" if habit != "swimming" else "Weekly")
            tracker.store(db)
            cursor.execute('SELECT id FROM habits WHERE name = ?', (habit,))
            habit_id = cursor.fetchone()[0]
        else:
            habit_id = habit_id[0]

        for date in dates:
            current_time = datetime.strptime(date, "%Y-%m-%d")
            cursor.execute('''INSERT INTO trackers (habit_id, increment_date)
                              VALUES (?, ?)''', (habit_id, current_time.strftime("%Y-%m-%d %H:%M:%S")))
            db.commit()


predefined_habits_db()



