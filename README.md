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
The application will display a menu with options.
Follow the on-screen prompts to interact with the application.

## Analysis Module

The analyze.py module provides a Habit Analysis tool, allowing users to perform various tasks related to habit analysis. The analysis tool is designed to work seamlessly with the Habit Tracker project.

### Usage

Run the Habit Analysis tool using:

```shell
python analyze.py
```

The Habit Analysis tool will display a menu. Follow the on-screen prompts to select and perform the desired analysis tasks.

### Notes
Ensure that the habit_tracker.py, database.py, and analyze.py modules are present and properly configured in your project for the analysis tool to work correctly.

## Running Unit Tests

To ensure the reliability and correctness of your Habit Tracker project, it's essential to write and run unit tests. Follow these steps to execute the unit tests for the project:

**Change Directory:**
Open your command prompt or terminal and navigate to the `tracker` directory using the following command:
```shell
cd habit_tracker_project_2023\tracker
```

Run Unit Tests:

Execute the following command to run the unit tests
```shell
python -m unittest -v test.py
```
If all tests pass, you should see a summary indicating the number of tests run and their status.

