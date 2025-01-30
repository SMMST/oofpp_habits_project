import questionary
from db import get_db,habit_by_periodicity, get_habits_list, get_tracker
from tracker import Tracker
from analyse import longest_streak_all_habits, calculate_longest_streak


def cli():
    db=get_db()

    # Greeting the user
    while not questionary.confirm("Welcome!Are you ready").ask():
        pass

    stop=False
    while not stop:
        choice= questionary.select(
            "What do you want to do?",
            choices=["Create a New Habit",
                     "Checkoff Habit",
                     "Analyse Habits",
                     "Delete Habit",
                      "Exit"]
        ).ask()
    
        if choice == "Create a New Habit":
            create_habit(db)
        elif choice == "Checkoff Habit":
            checkoff_habit(db)
        elif choice == "Analyse Habits":
            analyse_habits(db)
        elif choice == "Delete Habit":
            delete_habit(db)
        elif choice == "Exit":
         stop=True

# Habit management instructions for user

def create_habit(db):
    name = questionary.text("What is the name of your new habit?").ask()
    periodicity = questionary.select("Is this a Daily or a Weekly habit?", choices=["Daily", "Weekly"]).ask()
    tracker = Tracker(name, periodicity)
    tracker.store(db)
    print(f"Habit {"name"}created!")

def checkoff_habit(db):
    habits = get_habits_list(db)
    name = questionary.select("Which habit do you want to check off?").ask()
    tracker = get_tracker(db,name)
    tracker.checkoff(db)
    print(f"Habit {"name"} is checked off!")

def analyse_habits(db):
    analysis_choice = questionary.select(
        "Please choose from the list below what would you like to analyse?",
        choices=["List all habits",
                 "List habits by periodicity",
                 "Longest streak of all habits",
                 "Longest streak for a habit", "Exit"]).ask()

    if analysis_choice == "List all habits":
        habits = get_habits_list(db)
        print("Currently tracked habits:")
        for habit in habits:
            print(habit)


    elif analysis_choice == "List habits by periodicity":
        periodicity = questonary.select("Select the periodicity", choices=["Daily", "Weekly"]).ask()
        habits = habit_by_periodicity(db, periodicity)
        print(f"Tracked habits with {periodicity} periodicity:")
        for habit in habits:
            print(habit)

    elif analysis_choice == "Longest streak of all habits":
        streak = longest_streak_all_habits(db)
        print(f"The longest streak of all habits is {streak}.")

    elif analysis_choice == "Longest streak for a habit":
        habits = get_habits_list(db)
        name = questonary.select("Select the habit", choices=habits + ["Exit"]).ask()
        if name != "Exit":
            streak = calculate_longest_streak(db, name)
            print(f"The longest streak for habit '{name}' is {streak}.")
    elif analysis_choice == "Exit":
        return

def delete_habit(db):
    habits = get_habits_list(db)
    name = questionary.select("Which habit would you like to delete?", choises = habits +["Exit"]).ask()
    if name != "Exit":
        tracker = get_tracker(db,name)
        tracker.delete(db)
        print(f"Habit {"name"} deleted!")


if  __name__ == "__main__":
    cli()

