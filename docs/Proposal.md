# Proposed Deliverables for Milestone 3
---

# Table of Contents

1. [Core Features](#1-core-features)\
  1.1 [Dashboad](#11-dashboard)\
    1.1.1 [Progress tracking](#111-progress-tracking)\
    1.1.2 [To-do List](#112-todo-list)\
  1.2 [Pomodoro Timer](#12-pomodoro-timer)\
    1.2.1 [Countdown Clock](#121-countdown-clock)
2. [Database](#2-database)
3. [Testing](#3-testing)\
  3.1 [Django Unit Testing](#31-django-unit-testing)\
  3.2 [Authoring Functional Tests Using Selenium](#32-authoring-functional-tests-using-selenium)


# 1. Core Features

## 1.1 Dashboard

### 1.1.1 Progress tracking

#### Description

* User’s progress is displayed on the dashboard with each of their project and plan as one individual card. 
* User will be able to view immediately their progress quantitatively with a visualized progress bar and increase or decrease easily with the `+` and `-` buttons.
* User can edit their progress card name.

![New Dashboard](img/new_dashboard.png)

#### Implementation

* Client-side: write a VueJS component for each of the progress card that includes the following attributes:
  * `title` (string)
  * `progress` (integer)
  * `duration` (datetime)
  * `tag` (string)
* Write a Django model that has the same attribute as the VueJS component. The sever-side data will be updated calling a Django view function asynchronously (Ajax) using Vue.

### 1.1.2 To-do List

#### Description

* Users are able to have more options to customize their task: they can add a task tag (school, work, networking,...) and specify the level of urgency. The tags and level of urgency will be displayed beside the task title. Users will benefit from this feature in the sense that they will know which task needs finishing first and not get overwhelmed.
* Connect client-side and server-side data: currently, users are able to interact with the todo list, but data will be refreshed after each session. By the end of milestone 3, the to-do list will be bind to the user with the one-to-many relationship.

#### Implementation

* Expand the current `todolist` object (add tag and the level of urgency attributes).
* Write a Django model that has the same attribute as the `todolist` object. The server-side data will be updated by calling a Django view function asynchronously (Ajax) using Vue.


## 1.2 Pomodoro Timer

### 1.2.1 Countdown Clock

#### Description

* Current approach to focus cycle tracking: Currently, when the current mode is Pomodoro (focus) mode, if users stop the countdown clock, they might adjust the focus time using `+` and `-` buttons then resume. As a result, users can cheat to get their rewards, which might counteract the aim of the reward scheme.
* New way of cycle tracking: When users top the countdown clock in Pomodoro mode, they will have 2 options: `resume` and `restart`. Additionally, when in Pomodoro mode, users are unable to adjust the time using `+` and `-` buttons. If users choose to restart, they can start a new cycle, adjust the time to their liking, but the old cycle will be completely lost. This approach will motivate users to complete their current cycle and ban them from cheating.
* Overview/tracking cycle count: A comprehensive overview of the usage of the Pomodoro timer will be displayed to the user, which will give the user a broad view of their work/study.

#### Implementation

* Add new `resume` and `restart` buttons and bind their condition of appearance using VueJS.
* Write a Django model `Cycle` that has the following attributes `cycleCount`, `duration`, and `dateTime` to store the focus time into the database.

### 1.2.2 Countdown Clock

#### Description

* There will be a reward for each week, which is a random hidden picture. The picture will be revealed piece by piece based on the total focus time of the user.
* Users will also be able to see their progress in detail with a visualized dynamic progress bar.
* This will gamify the pomodoro module and motivate users to focus more.

![New Pomodoro](img/new_pomodoro.png)

#### Implementation

* The total focus time of the user will be stored in the database. The picture with the exact hidden pieces will be rendered based on that focus time.
* The total time focus bar is a Vuejs component bind with asynchronous data fetch from Django backend.

## 1.3 Calendar

### 1.3.1 Calendar Module

#### Description

* Users can connect their calendar with Google Calendar, they can export their existing schedule or sync ActiveNUS calendar and Google Calendar.
* Users can also export their schedule to `.ics` file so that they can import it to many other different calendar applications.

#### Implementation

* Call API from Google Calendar API to sync and read data from Google Calendar
* We are considering using `django-ical` or `ics` package to export `.ics` files.

### 1.3.2 Calendar Module

#### Description

* Within the calendar module, users have a choice to create a new progress, which will be reflected on the dashboard page. 
* Users can choose to or not to authorize ActiveNUS to automatically render a schedule, which will be based on the expected workload and expected number of iterations using active recall and spaced repetition logic

![New Calendar](img/new_calendar.png)

#### Implementation

The algorithm to generate schedules automatically will be written based on Ebbinghaus’ forgetting curve and review cycle. ActiveNUS will also have conditions to restrict the input data (for example end date must be at least 2 days after the start date, or the number of iterations must fall into some range based on the expected workload input,...). Based on the input data, ActiveNUS will generate calendar events.

## 1.4 Flashcard System

### 1.4.1 Flashcard Folder

#### Description

* Organizing flashcards by folder. Users will be able to see the number of items in each folder to have a broader overview of the subject. They can also add a new folder with the description on this page.
* For each folder, users have the option to edit and learn the topic

![New Flashcard](img/new_flashcard.png)

#### Implementation

* Create a new page to display folders.
* Each folder will have a specific view page with a parameter which is the `id` of the folder and will be handled by `django.urls`.

### 1.4.2 Algorithm to Optimize Flashcard Order

#### Description

* Instead of the option to go to the next or previous card, users will be asked about their familiarity with the item.
* The next flashcard will be rendered based on their level of familiarity with the topic.

![New Flashcard 1](img/new_flashcard1.png)

#### Implementation

Each card has score and number_of_attempts attributes. After each attempts, these attributes will be updated with the formula:

```python
score = (score * number_of_attempts + n) / (number_of_attempts + 1)

number_of_attempts = number_of_attempts + 1
```

The items in a folder are sorted by the score and displayed to the user in ascending order of score.

## 1.5 Social Forum (depends on the progress)

#### Description

* Find friends on ActiveNUS
* Write posts in the forum
* Comment on the others’ posts

#### Implementation

* Finding friends can be implemented by a database query.
* Writing posts and commenting functionalities will be handled by POST request and rendered to the website by a Vue model.


# 2. Database

Currently, data is stored in local storage, except Users’ profiles are stored in SQLite3 database (server-side). By milestone 3, we will store all the data in the server-side database.

In addition, we are considering using PostgreSQL to store and manage data for the final product instead of SQLite3 since PostgreSQL is more compatible with Heroku and can manage a larger amount of data.


# 3. Testing

## 3.1 Django Unit Testing

Along with completing the main components, we also write test functions for features with the same approach taken in milestone 2 using `django.test` module.

The tests include:

* Checking models (valid methods and attributes)
* Checking client-side (assert the HTTP status codes and the messages to the client)
* Checking logic (the algorithms of schedule suggestion and rendering flashcards to the users based on their level of familiarity with the topic)

## 3.2 Authoring Functional Tests Using Selenium

Since ActiveNUS consists of many components, it is difficult to test the client-side code manually. Therefore, we will use Selenium WebDriver, which is a collection of open-source APIs, to automate the testing of the web application.

To use Selenium and ChromeDriver, we need to install these 2 libraries into our environment by running `pip install selenium` and `pip install chromedriver-py`.

Basic setup:

```python
import os
import pathlib
import unittest

from selenium import webdriver

# Finds the Uniform Resourse Identifier of a file
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Sets up web driver using Google chrome
driver = webdriver.Chrome()
```

Then we can use the driver to simulate automated tests of our page.