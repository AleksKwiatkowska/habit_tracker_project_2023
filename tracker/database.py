import sqlite3
from habit import Habit
from datetime import datetime

class HabitDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                frequency TEXT NOT NULL,
                category TEXT NOT NULL,
                created_at DATETIME NOT NULL,
                last_checked DATETIME,
                streak INTEGER
            )
        ''')
        self.conn.commit()

    def add_habit(self, name, frequency, category):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO habits (name, frequency, category, created_at, last_checked, streak)
            VALUES (?, ?, ?, DATETIME('now'), DATETIME('now'), 0)
        ''', (name, frequency, category))
        self.conn.commit()

    def get_habit_by_name(self, name):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM habits WHERE name = ?', (name,))
        row = cursor.fetchone()
        if row:
            id, name, frequency, category, created_at, last_checked, streak = row
            habit = Habit(name, frequency, category)
            habit.created_at = created_at
            habit.last_checked = last_checked
            habit.streak = streak
            return habit
        return None

    def get_all_habits(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM habits')
        habits = []
        for row in cursor.fetchall():
            id, name, frequency, category, created_at, last_checked, streak = row
            habit = Habit(name, frequency, category)
            habit.created_at = created_at
            habit.last_checked = last_checked
            habit.streak = streak
            habits.append(habit)
        return habits
