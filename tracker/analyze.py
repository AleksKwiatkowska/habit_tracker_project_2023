from habit_tracker import HabitTracker
from database import HabitDatabase
from datetime import datetime, timedelta

class HabitAnalysis:
    def __init__(self, habit_database):
        self.habit_database = habit_database
        self.run()

    def run(self):
        """
        Main loop for the Habit Analysis tool.
        Allows the user to perform various habit analysis tasks.
        """
        while True:
            print("\nHabit Analysis Menu:")
            print("1. Find longest habit streak")
            print("2. List current daily habits")
            print("3. List all tracked habits")
            print("4. List habits with same frequency")
            print("5. Longest run streak for a given habit")
            print("6. Completions within the last days")
            print("7. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.find_longest_streak()
            elif choice == "2":
                self.list_current_daily_habits()
            elif choice == "3":
                self.list_all_tracked_habits()
            elif choice == "4":
                self.list_habits_with_same_frequency()
            elif choice == "5":
                habit_name = input("Enter the habit name: ")
                self.longest_run_streak_for_habit(habit_name)
            elif choice == "6":
                days = int(input("Enter the number of days: "))
                self.completions_within_timeframe(days)
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def find_longest_streak(self):
        """
        Find and display the longest habit streak among all habits.
        """
        habits = self.habit_database.get_all_habits()
        longest_streak = 0
        longest_streak_habit = None

        for habit in habits:
            if habit.streak > longest_streak:
                longest_streak = habit.streak
                longest_streak_habit = habit

        if longest_streak_habit:
            print(f"Longest habit streak: {longest_streak} days for habit '{longest_streak_habit.name}'")
        else:
            print("No habits found.")

    def list_current_daily_habits(self):
        """
        List habits that have a daily frequency (frequency = 1).
        """
        habits = self.habit_database.get_all_habits()
        daily_habits = [habit for habit in habits if habit.frequency == 1]

        if daily_habits:
            print("Current daily habits:")
            for habit in daily_habits:
                print(f"Habit: {habit.name}, Streak: {habit.streak}")
        else:
            print("No daily habits found.")

    def list_all_tracked_habits(self):
        """
        List all habits tracked in the database.
        """
        habits = self.habit_database.get_all_habits()
        if habits:
            print("All tracked habits:")
            for habit in habits:
                print(f"Habit: {habit.name}")
        else:
            print("No habits found.")

    def list_habits_with_same_frequency(self):
        """
        List habits with the same specified frequency.
        """
        frequency = input("Enter the frequency (e.g., 1, 7, 14 etc.): ")
        habits = self.habit_database.get_habit_by_frequency(frequency)
        if habits:
            print(f"Habits with {frequency} frequency:")
            for habit in habits:
                print(f"Habit: {habit.name}")
        else:
            print(f"No {frequency} habits found.")

    def longest_run_streak_for_habit(self, habit_name):
        """
        Find and display the longest run streak for a specific habit.
        """
        habit = self.habit_database.get_habit_by_name(habit_name)
        if habit:
            print(f"Longest run streak for '{habit_name}': {habit.streak} days")
        else:
            print(f"No habit found with the name '{habit_name}'.")

    def completions_within_timeframe(self, days):
        """
        Count and display the number of habit completions within the specified time frame.
        """
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days)
        habits = self.habit_database.get_all_habits()
        completions = 0

        for habit in habits:
            if habit.last_checked is not None:
                last_checked_date = datetime.strptime(habit.last_checked, '%Y-%m-%d').date()
                if start_date <= last_checked_date <= end_date:
                    completions += 1

        print(f"Completions within the last {days} days: {completions}")

if __name__ == "__main__":
    habit_database = HabitDatabase('my_habits.db')
    habit_analysis = HabitAnalysis(habit_database)
