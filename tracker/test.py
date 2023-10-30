import unittest
from datetime import date, timedelta
from habit import Habit
from habit_tracker import HabitTracker

class TestHabit(unittest.TestCase):
    def test_mark_habit_completed(self):
        """
        Test the 'mark_habit_completed' method of the Habit class.
        """
        # Create a habit with daily frequency
        habit = Habit("Test Habit", 1, "Test Category")

        # Mark habit as completed for today
        habit.mark_habit_completed()
        self.assertEqual(habit.streak, 1)
        self.assertEqual(habit.last_checked, date.today())

        # Mark habit as completed again today (should not change streak)
        habit.mark_habit_completed()
        self.assertEqual(habit.streak, 1)

        # Mark habit as completed for the next day (should increase streak)
        habit.last_checked = date.today() - timedelta(days=1)
        habit.mark_habit_completed()
        self.assertEqual(habit.streak, 2)
        self.assertEqual(habit.last_checked, date.today())

    def test_check_streak(self):
        """
        Test the 'check_streak' method of the Habit class.
        """
        # Create a habit with daily frequency
        habit = Habit("Test Habit", 1, "Test Category")
        self.assertEqual(habit.check_streak(), 0)

        # Mark habit as completed for consecutive days
        habit.mark_habit_completed()
        self.assertEqual(habit.check_streak(), 1)

        habit.last_checked = date.today() - timedelta(days=1)
        habit.mark_habit_completed()
        self.assertEqual(habit.check_streak(), 2)

class TestHabitTracker(unittest.TestCase):
    def test_add_habit(self):
        """
        Test the 'add_habit' method of the HabitTracker class.
        """
        # Create a HabitTracker instance
        tracker = HabitTracker()

        # Add a habit to the tracker
        habit = tracker.add_habit("Test Habit", 1, "Test Category")

        # Check if the habit was added and is an instance of Habit
        self.assertIsInstance(habit, Habit)
        self.assertEqual(len(tracker.habits), 1)
