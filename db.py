import sqlite3
from tracker import Tracker


def get_db():
    """ Initialize the data connection"""
    db =  sqlite3.connect("main.db")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        periodicity TEXT NOT NULL,
        start_date TEXT
        )""")

    cursor.execute("""CREATE A TABLE IF NOT EXISTS trackers( 
        id INTEGER PRIMARY KEY,
        habit_id INTEGER,
        checkoff_date TEXT,
        FOREIGN KEY (habit_id) REFERENCES habits(id)
        )""")

    db.commit()
    """Return the data connection """
    return db


def get_habits_list(db):
    """Function for extracting the habit names from database"""
    cursor = db.cursor()
    cursor.execute("SELECT name FROM habits")
    rows = cursor.fetchall()
    return[row[0]for row in rows]

def habit_by_periodicity(db, periodicity):
    """Function for extring habit names by periodicity"""
    cursor = db.cursor()
    cursor.execute("""SELECT name FROM habits WHERE periodicity =?""",periodicity)
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def get_tracker(db,name):
    """Function for extracting the Tracker object by  specific habit name"""
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM habits WHERE name = ?""", name)
    habit = cursor.fetchone()
    if habit:
        return Tracker(habit[1], habit[2], habit[3], habit[0])
    else:
        return None