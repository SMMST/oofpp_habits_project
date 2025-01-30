import sqlite3
from tracker import Tracker
from datetime import datetime, timedelta
from db import get_habits_list
from analyse import calculate_longest_streak


def setup_database():
    db = sqlite3.connect(":memory:")
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE habits (
                        id INTEGER PRIMARY KEY,
                        name TEXT UNIQUE NOT NULL,
                        periodicity TEXT NOT NULL,
                        creation_date TEXT
                    )''')
    cursor.execute('''CREATE TABLE trackers (
                        id INTEGER PRIMARY KEY,
                        habit_id INTEGER,
                        checkoff_date TEXT,
                        FOREIGN KEY (habit_id) REFERENCES habits (id)
                    )''')
    return db


def test_create_habit():
    db = setup_database()
    tracker = Tracker("Test Habit", "This is a test habit", "Daily")
    tracker.store(db)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM habits WHERE name = 'Test Habit'")
    habit = cursor.fetchone()
    assert habit is not None
    assert habit[0] == "Test Habit"


def test_checkoff_habit():
    db = setup_database()
    tracker = Tracker("Pilates", "Exercise", "Daily")
    tracker.store(db)
    tracker.checkoff(db)
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM trackers WHERE habit_id = ?", (tracker.id,))
    count = cursor.fetchone()[0]
    assert count == 1


def test_calculate_longest_streak():
    db = setup_database()
    tracker = Tracker("Running", "Sleeping", "Daily")
    tracker.store(db)

    checkoff_date1 = datetime.now() - timedelta(days=2)
    checkoff_date2 = datetime.now() - timedelta(days=1)
    cursor = db.cursor()
    cursor.execute('''INSERT INTO trackers (habit_id, checkoff_date)
                          VALUES (?, ?)''', (tracker.id, checkoff_date1.strftime("%Y-%m-%d %H:%M:%S")))
    cursor.execute('''INSERT INTO trackers (habit_id, checkoff_date)
                          VALUES (?, ?)''', (tracker.id, checkoff_date2.strftime("%Y-%m-%d %H:%M:%S")))
    db.commit()

    tracker2 = Tracker("Pilates", "Exercise", "Daily")
    tracker2.store(db)
    tracker2.checkoff(db)


if __name__ == "__main__":
    test_create_habit()
    test_checkoff_habit()
    test_calculate_longest_streak()

