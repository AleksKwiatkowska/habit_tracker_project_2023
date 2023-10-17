from datetime import datetime

class Habit:
    """
    Represents a habit to be tracked.

    Attributes:
        name (str): The name of the habit (e.g., "Drink a glass of water").
        frequency (str): The frequency of the habit (e.g., "daily").
        category (str): The category of the habit (e.g., "Health").
        created_at (datetime): The date and time when the habit was created.
        completion_history (list): A list of completion dates for streak tracking.
    """

    def __init__(self, name, frequency, category):
        """
        Initializes a new habit.

        Args:
            name (str): The name of the habit.
            frequency (str): The frequency of the habit.
            category (str): The category of the habit.
        """
        self.name = name
        self.frequency = frequency
        self.category = category
        self.created_at = datetime.now()
        self.completion_history = []

    def mark_habit_completed(self):
        """
        Marks the habit as completed for the current date and time.
        """
        completed_date = datetime.now()
        self.completion_history.append(completed_date)

    def check_streak(self):
        """
        Checks the current streak of consecutive completions.

        Returns:
            int: The number of days in the current streak.
        """
        if not self.completion_history:
            return 0

        current_date = datetime.now()
        last_completion_date = self.completion_history[-1]
        delta = current_date - last_completion_date

        return delta.days

# Example usage:
# habit = Habit("Drink a glass of water", "daily", "Health")
# habit.mark_habit_completed()
# streak = habit.check_streak()
# print(f"Habit: {habit.name}. Streak: {streak} days.")
   # Last completed on {last_completion_date}."
