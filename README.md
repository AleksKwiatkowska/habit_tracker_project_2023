# My Habit Tracker Project

This project is the final assignment for the "Object-oriented and Functional Programming with Python" course at IU Akademie. Developed in 2023 as part of Weiterbildung "Data Analyst - Python."

## What it is?

The Habit Tracker is a Python application designed to help users manage and monitor their habits. It allows you to add new habits, mark them as completed, and list all tracked habits, providing insights into your progress and streaks.

## Installation

```shell
git clone https://github.com/AleksKwiatkowska/habit_tracker_project_2023.git
cd habit_tracker_project_2023
pip install -r requirements.txt
```

## Usage

Initialize

```shell
python habit.py
python habit_tracker.py
python database.py
```

Then, start:

```shell
python main.py
```

and follow instructions on the screen.
The application will display a menu with options to:

Add a Habit
Mark a Habit as Completed
List All Habits
Quit
Follow the on-screen prompts to interact with the application.

## Analysis Module - `analyze.py`

The analyze.py module provides a Habit Analysis tool, allowing users to perform various tasks related to habit analysis. The analysis tool is designed to work seamlessly with the Habit Tracker project.

### Usage

Run the Habit Analysis tool using:

```shell
python analyze.py
```

The Habit Analysis tool will display a menu with the following options:

Find longest habit streak
List current daily habits
List all tracked habits
List habits with the same frequency
Longest run streak for a given habit
Completions within the last days
Quit
Follow the on-screen prompts to select and perform the desired analysis tasks.

### Notes
Ensure that the habit_tracker.py, database.py, and analyze.py modules are present and properly configured in your project for the analysis tool to work correctly.
