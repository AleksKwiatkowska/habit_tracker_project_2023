from habit import Habit

class HabitTracker:
    """
    Manages a list of habits and provides methods for habit management.

    Attributes:
        habits (list): A list of Habit objects.
    """
    def __init__(self):
        """
        Initializes a new HabitTracker with an empty list of habits.
        """
        self.habits = []

    def add_habit(self, name, frequency, category):
        """
        Adds a new habit to the tracker.

        Args:
            name (text): The name of the habit.
            frequency (int): The frequency of the habit.
            category (text): The category of the habit.

        Returns:
            Habit: The newly created Habit object.
        """
        habit = Habit(name, frequency, category)
        self.habits.append(habit)
        return habit

    def mark_habit_completed(self, habit):
        """
        Marks a habit as completed for the current date.

        Args:
            habit (Habit): The Habit object to be marked as completed.
        """
        habit.mark_habit_completed()

    def list_habits(self):
        """
        Returns a list of all habits currently tracked.

        Returns:
            list: A list of Habit objects.
        """
        return self.habits
    