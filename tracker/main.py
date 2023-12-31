from habit import Habit
from habit_tracker import HabitTracker
from database import HabitDatabase
from datetime import datetime

class Main:
    def __init__(self):
        self.habit_database = HabitDatabase('my_habits.db')
        self.run()

    def run(self):
        """
        Main loop for the Habit Tracking App.
        Allows the user to perform various actions on habits.
        """
        while True:
            print("\nHabit Tracking App Menu:")
            print("1. Add a Habit")
            print("2. Mark Habit as Completed")
            print("3. List All Habits")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_habit()
            elif choice == "2":
                self.mark_habit_completed()
            elif choice == "3":
                self.list_habits()
            elif choice == "4":
                self.habit_database.conn.close()
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def add_habit(self):
        """
        Add a new habit to the database.
        Prompts the user for the habit's name, frequency, and category.
        """
        name = input("Enter the name of the habit: ")
        frequency = input("Enter the frequency of the habit as a number (1 for daily habits, 7 for weekly habits etc.): ")
        category = input("Enter the category of the habit: ")

        self.habit_database.add_habit(name, frequency, category)

    def mark_habit_completed(self):
        """
        Mark a habit as completed and update its streak.
        Prompts the user for the habit's name and updates the database.
        """
        name = input("Enter the name of the habit you completed: ")

        habit = self.habit_database.get_habit_by_name(name)

        if habit:
            habit.mark_habit_completed()
            self.habit_database.conn.execute('''
                UPDATE habits
                SET last_checked = ?, streak = ?
                WHERE name = ?
            ''', (habit.last_checked, habit.streak, habit.name))
            self.habit_database.conn.commit()
            print(f"You've completed the habit: {habit.name}")
        else:
            print("Habit not found.")

    def list_habits(self):
        """
        List all habits in the database with their details.
        """
        habits = self.habit_database.get_all_habits()
        if habits:
            print("Habits in the Database:")
            for habit in habits:
                streak = habit.streak
                print(f"Name: {habit.name}, Frequency: {habit.frequency}, Category: {habit.category}, Streak: {streak}")
        else:
            print("No habits found in the database.")

if __name__ == "__main__":
    main = Main()