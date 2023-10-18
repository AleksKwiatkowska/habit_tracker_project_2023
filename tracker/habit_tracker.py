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
            name (str): The name of the habit.
            frequency (str): The frequency of the habit.
            category (str): The category of the habit.

        Returns:
            Habit: The newly created Habit object.
        """
        habit = Habit(name, frequency, category)
        self.habits.append(habit)
        return habit

    def edit_habit(self, habit, new_name, new_frequency, new_category):
        """
        Edits the properties of an existing habit.

        Args:
            habit (Habit): The Habit object to be edited.
            new_name (str): The new name for the habit.
            new_frequency (str): The new frequency for the habit.
            new_category (str): The new category for the habit.
        """
        habit.name = new_name
        habit.frequency = new_frequency
        habit.category = new_category

    def mark_habit_completed(self, habit):
        """
        Marks a habit as completed for the current date and time.

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
    