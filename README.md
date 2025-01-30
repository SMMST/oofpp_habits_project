# My Habit Tracker App Project 

The Habit Tracker App Project is created by Python Object-Oriented and Functional Programming.
## Description

In this project is created habit tracker application with basic Command Line Interface(CLI), which enable the user to
track,check off, add, delete and analyse his habits on daily or weekly basis within four weeks and has insight in their streaks or breaks.
This application is created, implemented and tested in Python 3.13.
The code is running by the "main.py" file and the user just follow the instructions on the screen.
For testing the App, the user already have  five stored predefined habits on disposal.
This basic App concept is suitable for further development  and implementing Graphic User Interface (GUI).

## Installation

```shell
- Download the GitHub repository:  https://github.com/SMMST/oofpp_habits_project   
- run the command: 
  pip install-r requirements.txt
```
## Usage
To start the App, user simply run command: 
```shell
python main.py
```
and follow the instructions on screen:

1.  Choose some of the five already stored habits to test the App: 
    - Running: Daily
    - Meditating: Daily
    - Swimming: Weekly 
    - Reading book: Weekly
    - Walking in nature: Weekly
  
2. Create a New Habit: add the new habit to track menu:
    - select: "Create a new habit"
    - type the name of the new habit
    - choose the periodicity from the offered " Daily" or "Weekly" choices
    - the new habit is created and stored
    - 
3. Check off Habit: Mark your habit as completed for the specified date.
    - select:"Check off Habit"
    - select the habit that you completed
    - the last check off date is updated
   
4. Analyse Habits: Review your tracked habits and its longest streaks.
    - select: "Analyse Habit"
      - select: - "Longest streak for a habit"
                - "Longest streak for all habits"
 - Delete Habit:
   - select: "Delete Habit"
   - select the habit you want to delete
   - the habit is deleted from database
 - Exit: leave the App.
 

## Tests
In order to test the App function, the module test_project.py is used, by running the command:

```shell
pytest .

``` 






