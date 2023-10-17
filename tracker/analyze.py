from habit_tracker import HabitTracker
from database import HabitDatabase
from datetime import datetime, timedelta  # Import timedelta for time frame calculations

class HabitAnalysis:
    def __init__(self, habit_database):
        self.habit_database = habit_database
        self.run()

    def run(self):
        while True:
            print("\nHabit Analysis Menu:")
            print("1. Find Longest Habit Streak")
            print("2. List Current Daily Habits")
            print("3. Completions within a Time Frame")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.find_longest_streak()
            elif choice == "2":
                self.list_current_daily_habits()
            elif choice == "3":
                days = int(input("Enter the number of days: "))  # Prompt for the number of days
                self.completions_within_timeframe(days)  # Pass the 'days' argument
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def find_longest_streak(self):
        habits = self.habit_database.get_all_habits()
        longest_streak = 0
        longest_streak_habit = None

        for habit in habits:
            if habit.streak > longest_streak:
                longest_streak = habit.streak
                longest_streak_habit = habit

        if longest_streak_habit:
            print(f"Longest Habit Streak: {longest_streak} days for habit '{longest_streak_habit.name}'")
        else:
            print("No habits found.")

    def list_current_daily_habits(self):
        habits = self.habit_database.get_all_habits()
        daily_habits = [habit for habit in habits if habit.frequency == 1]

        if daily_habits:
            print("Current Daily Habits:")
            for habit in daily_habits:
                print(f"Habit: {habit.name}, Streak: {habit.streak}")
        else:
            print("No daily habits found.")

    def completions_within_timeframe(self, days):
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days)
        habits = self.habit_database.get_all_habits()
        completions = 0

        for habit in habits:
            for completion_date in habit.completion_history:
                if start_date <= completion_date.date() <= end_date:
                    completions += 1

        print(f"Completions within the last {days} days: {completions}")

if __name__ == "__main__":
    habit_database = HabitDatabase('my_habits.db')  # Adjust the database file path as needed
    habit_analysis = HabitAnalysis(habit_database)
