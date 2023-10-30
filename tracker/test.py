import unittest
from datetime import date, timedelta
from habit import Habit
from habit_tracker import HabitTracker

class TestHabit(unittest.TestCase):
    def test_mark_habit_completed(self):
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
        tracker = HabitTracker()
        habit = tracker.add_habit("Test Habit", 1, "Test Category")
        self.assertIsInstance(habit, Habit)
        self.assertEqual(len(tracker.habits), 1)

    def test_mark_habit_completed(self):
        tracker = HabitTracker()
        habit = tracker.add_habit("Test Habit", 1, "Test Category")
        habit.mark_habit_completed()
        self.assertEqual(habit.streak, 1)

    def test_list_habits(self):
        tracker = HabitTracker()
        habit1 = tracker.add_habit("Habit 1", 1, "Category 1")
        habit2 = tracker.add_habit("Habit 2", 2, "Category 2")

        habit_list = tracker.list_habits()
        self.assertIsInstance(habit_list, list)
        self.assertEqual(len(habit_list), 2)
        self.assertIn(habit1, habit_list)
        self.assertIn(habit2, habit_list)

if __name__ == '__main__':
    unittest.main()
