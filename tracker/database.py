import sqlite3
from habit import Habit
from datetime import datetime

class HabitDatabase:
    def __init__(self, db_name):
        """
        Initialize the HabitDatabase class.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """
        Create the 'habits' table in the database if it doesn't exist.
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                frequency INTEGER NOT NULL,
                category TEXT NOT NULL,
                created_at DATE NOT NULL,
                last_checked DATE,
                streak INTEGER
            )
        ''')
        self.conn.commit()

    def add_habit(self, name, frequency, category):
        """
        Add a new habit to the 'habits' table.

        Args:
            name (text): The name of the habit.
            frequency (int): The frequency of the habit.
            category (text): The category of the habit.
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO habits (name, frequency, category, created_at, last_checked, streak)
            VALUES (?, ?, ?, DATE('now'), DATE('now'), 0)
        ''', (name, frequency, category))
        self.conn.commit()

    def get_habit_by_name(self, name):
        """
        Retrieve a habit by its name.

        Args:
            name (text): The name of the habit to retrieve.

        Returns:
            Habit: A Habit object representing the habit, or None if not found.
        """
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
    
    def get_habit_by_frequency(self, frequency):
        """
        Retrieve habits with a specific frequency.

        Args:
            frequency (int): The frequency of habits to retrieve.

        Returns:
            list: A list of Habit objects with the specified frequency.
        """
        habits = []
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM habits WHERE frequency = ?', (frequency,))
        rows = cursor.fetchall()
        
        for row in rows:
            id, name, frequency, category, created_at, last_checked, streak = row
            habit = Habit(name, frequency, category)
            habit.created_at = created_at
            habit.last_checked = last_checked
            habit.streak = streak
            habits.append(habit)

        return habits

    def get_all_habits(self):
        """
        Retrieve all habits stored in the database.

        Returns:
            list: A list of all Habit objects in the database.
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM habits')
        habits = []
        for row in cursor.fetchall():
            id, name, frequency, category, created_at, last_checked, streak = row
            habit = Habit(name, frequency, category)
            habit.created_at = created_at
            # Set last_checked to None for habits retrieved from the database
            habit.last_checked = None if last_checked is None else datetime.strptime(last_checked, '%Y-%m-%d').date()
            habit.streak = streak
            habit.frequency = frequency
            habits.append(habit)
        return habits
    

