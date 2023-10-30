from datetime import datetime, date

class Habit:
    """
    Represents a habit to be tracked.

    Attributes:
        name (text): The name of the habit (e.g., "Drink a glass of water").
        frequency (int): The frequency of the habit (e.g., "1").
        category (text): The category of the habit (e.g., "Health").
        created_at (date): The date when the habit was created.
        last_checked (date): The date when the habit was last checked (i.e. completed).
        streak (int): The current streak of consecutive completions.
    """

    def __init__(self, name, frequency, category, id=None):
        """
        Initializes a new habit.

        Args:
            name (text): The name of the habit.
            frequency (int): The frequency of the habit.
            category (text): The category of the habit.
        """
        self.id = id
        self.name = name
        self.frequency = frequency
        self.category = category
        self.created_at = date.today()
        self.last_checked = None
        self.streak = 0
        
    def mark_habit_completed(self):
        """
        Marks the habit as completed for the current date and updates the streak.
        """
        completed_date = date.today()

        if self.last_checked:
            days_difference = (completed_date - self.last_checked).days

        # Check if the habit hasn't been checked for the same date
            if days_difference == 1:
                self.streak += 1
            elif days_difference == 0:
            # If the habit was already checked today, do not increase the streak
                pass
            else:
                self.streak = 1
        else:
        # If last_checked is None, it's the first completion
            self.streak = 1
        self.last_checked = completed_date
     
    def check_streak(self):
        """
        Checks the current streak of consecutive completions.

        Returns:
            int: The number of days in the current streak.
        """
        return self.streak
