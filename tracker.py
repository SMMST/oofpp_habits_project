from datetime import datetime


class Tracker:


    def __init__(self, name,periodicity,id = None):

        """Habit class to track habit events.
                Initialize attributes to describe a´the habit.

                :param name: the name of the habit
                :param periodicity: periodicity of the habits, daily or weekly"""

        self.id = id
        self.name = name
        self.periodicity = periodicity
        self.start_date = datetime.now().strftime(" %Y-%m-%d %H:%M:%S ")

       #Instance methods:
    def checkoff(self,db,checkoff_date = None):
        """Checking off the completed habits"""
        cursor = db.cursor()
        if checkoff_date is None:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            current_time = checkoff_date.strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""INSERT INTO trackers(habit_id, checkoff_date)
                VALUES (?,?)""", (self.id, current_time))
        db.commit()


    def store(self,db):
        """Stores the habits in the database"""
        cursor = db.cursor()
        cursor.execute("""INSERT INTO habits (name, periodicity)
            VALUES (?,?)""" , (self.name, self.periodicity))
        db.commit()



    def delete(self,db):
        """Delete the habits from the database"""
        cursor = db.cursor()
        cursor.execute(""" DELETE FROM habits WHERE id = ? """, (self.id,))
        cursor.execute("""DELETE FROM trackers WHERE habit_id = ?""", (self.id,))
        db.commit()