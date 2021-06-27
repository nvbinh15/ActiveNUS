![ActiveNUS](img/logo+icon.png)

# 1. Deployment
[activenus.herokuapp.com](https://activenus.herokuapp.com/){:target="_blank"}

# 2. Testing Account
Username: test
Password: testingexamplepassword

# 3. Video
## 3.1 Introduction
[![Introduction Video](img/intro_thumbnail.png)](https://youtu.be/ZSS92-gmpTY){:target="_blank"}

## 3.2 Demo
(Video thumbnail + link)

# 4. Proposed Level of Achievement
Apollo 11

# 5. Motivation
A lot of students, especially university/college students, have frequent problems with study planning. They end up panicking, don’t know where to begin, and finally do not prepare well, which is the main reason for bad performances in tests and examinations.

Some are able to plan their study using available timetable-making applications in the market. However, few of these tools actually know what users need, and most of them are not optimal for learning management. Why isn’t there a tool that can help you keep track of your learning process and plan your study in a productive way?

# 6. Value Proposition
We hope to make a website that helps users, especially students, plan for work and study in general and promotes efficient study methods, namely active recall and spaced repetition.

The science behind active recall and spaced repetition:
* Active recall is the process of actively drawing information from your memory. It is a proven efficient way of moving knowledge from short-term to long-term memory compared to traditional passive revision, namely rereading, highlighting, etc. 
* Spaced repetition entails spacing the revision of the topics at specific intervals over time, which is proven to be beneficial by the 'forgetting curve.' We can take advantage of the forgetting curve by breaking the cycle by reviewing material at spaced intervals. The more we practice and the more spaced this repetition becomes, we will likely encode this information into our long-term memory.

How is active recall and spaced repetition incorporated into ActiveNUS:
* Calendar: our calendar has a built-in schedule recommendation feature based on the logic of spaced repetition and forgetting curve, helping students plan their studies more efficiently. 
* Flashcards:
  * Active recall is highly encouraged by flashcards. Flashcard is an effective and fun strategy for students to test themselves and utilize their cognitive power more actively
  * Spaced repetition: our flashcard module employs an algorithm that automatically renders a sequence of flashcards based on users’ feedback. The time interval between studying each flashcard will be optimized by the spaced repetition method.

# 7. How are we different from state-of-the-art platforms?

## 7.1 Google Calendar: 
The Calendar application of ActiveNUS has a recommendation system based on active recall and spaced repetition. The users will be provided the most effective study schedule.

## 7.2 Quizlet: 
Our flashcard system employs an underlying algorithm to sort items according to users’ familiarity with their contents.

## 7.3 Pomofocus: 
Our Pomodoro module is not a stand-alone count-down timer, but a useful part of a highly interconnected system. Each successful focus cycle is recorded and updated automatically to the Calendar module.

# 8. Tech Stack
Frontend
* HTML/CSS/JavaScript
* VueJS

Backend & Database
* Python
* Django
* SQLite

Server Deployment
* Heroku

# 9. Target user profile
* Users who prefer managing their schedule digitally
* Students approaching exam period
* Students who want to incorporate active recall and spaced repetition methods into their studying routines
* Students who want to use effective revision methods
* Users who want to have a platform to share and learn from the others

# 10. User Stories

(table)

# 11. Overall Design

We aim to make a website that helps users, especially students, plan for work and study in general and promotes efficient study methods, namely active recall and spaced repetition. To achieve this goal, we came up with the overall design for ActiveNUS.

## 11.1 Core Features

**Dashboard:** a comprehensive overview of your work/study progress and daily tasks 

**Calendar:** help you plan and track your studies with built-in active recall and spaced repetition logic.
* Export iCalendar file so that users can sync with other platforms (e.g. Google Calendar)
* User-friendly GUI to add a study session and categorize it based on modules or topics
* Tracking is enhanced by options to evaluate the studying session (how familiar the user is with the topic after revising).

**User account and Social Forum:** which user can create to save their progress and calendar and interact with friends
* Find friends on ActiveNUS
* Write posts in the forum, react and comment on the others’ posts

**Pomodoro timer:**
* A timer that runs for a default period of 25 minutes focus time and 5 minutes break (user has the option to make adjustment). 
* Each successful studying cycle will be recorded into the tracking calendar. Most of the administrative work is automatically done for the users.
* Send a notification at the system level (when the user is navigating outside the website)
* Users will be rewarded for each successful attempt.

**Flashcards systems:** Flashcard is an indispensable component of the active recall studying method
* Create folders of flashcards based on the topic you are studying for. 
* Accessing the flashcards folder for the topic or module directly from the dashboard

## 11.2 User Interface Design
ActiveNUS’s main target users are students and young people. Therefore, we choose a modern design language for the platform. Furthermore, we also promote simplicity in design, helping users get the best experience of learning and working with ActiveNUS.
The UI style guide and prototypes are included below.

![UI Guide](img/ui_guide.png)

![Prototypes](img/prototypes.png)

# 12. Project Scopes
The project is broken down into 3 parts corresponding to 3 milestones.

## 12.1 Milestone 1: Setting up authentication and administration

12.1.1 Set up application components (Authentication, Dashboard, Admin)

12.1.2 Frontend Web Routing: Set up URLs for the components of the applications 

```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('', include('dashboard.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
```

12.1.3 Set up Database using SQLite3. Models and data are stored in db.sqlite3 file.

12.1.4 Set up administration: using Django default admin app and creating a superuser.

![Admin](img/admin.png)

12.1.5 Token Authentication: implement user registration and login. Users will be able to register (email verification required), and upon logging in, are authenticated and assigned a token, their password will be hashed (instead of being stored as plain text directly).

![Register](img/register.png)

## 12.2 Building the core

### 12.2.1 Dashboard

**Description**

When a user is successfully logged in, he/she is taken to a dashboard page, which displays a comprehensive overview of the user's long-term progress and daily to-do list. Users are able to manually add/delete tasks and sort tasks according to their states. 

![Dashboard](img/dashboard.png)

**Consideration**

To-do list design consideration: On using to-do list, users might want to keep track of finished items but not delete them immediately. Therefore, we separate the remove button, which is minimally stylized as a trashcan and the finish toggle button.

Additionally, users can also have an option to move finished tasks to the end. This will be very helpful because in real-life usage, the order users add tasks and finish them are not the same. Hence, users can easily see at a glance which are the undone and done tasks separately. 

### 12.2.2 Pomodoro timer

**Description**

Users can navigate to the Pomodoro timer module with the navigation bar on the left. Pomodoro timer can now be used as a stand-alone feature. Users can simply press start and the timer will run for a default amount of 25 minutes. After 25 minutes of working, the user will move on to break mode. 

The focused time is recorded into local storage for future development. 

If the user wants more focus or break time, he/she can easily adjust with plus/minus buttons next to the countdown clock. The maximum time is set at 90 minutes and the minimum is 5 minutes.

After each cycle, the user receives a notification via the browser.

![Pomodoro](img/timer.png)

**Consideration**

At first our Pomodoro timer is designed with 4 buttons according to 4 different modes. The time designated for each mode is fixed at 25 minutes, 5 minutes and 15 minutes. This may cause irritation for users who want to change the focus and break time according to their needs.

Also, the 4 buttons structure in our first prototype are not intuitive for new users. Specifically, on their first encounter, without instruction, users may take a while to figure out which button corresponds to which mode and how to start a focus cycle.

Hence, in our second prototype, we replace the 4 buttons structures with a simple and intuitive start/stop toggle button and 3 buttons corresponding to 3 different modes to choose from. Furthermore, to increase more control for users, we include the plus and minus buttons for users to customize their cycle.

![Prev_timer](img/prev_timer.png)

### 12.2.3 Calendar

**Description**

Apart from viewing daily tasks and long-term progress, users can view their schedule more comprehensively in terms of date by navigating to their calendar.

Users now can add, drag and drop to update and delete events. Users can have different view modes to cater for their needs: monthly, weekly and daily view.

![Calendar](img/calendar.png)

**Consideration**

On view the calendar, users might want to view their schedule for the whole month or their daily detailed events. We take this into account during designing the calendar module so that users can easily navigate between different view modes (month, week and day) by using a button cluster on the top right.

Users can navigate easily between previous/next month, week or day using the 2 arrows on the top left. Also, users might want to immediately return to today’s date, hence, we add a ‘today’ button next to the arrow buttons.

### 12.2.4 Flashcard

**Description**

Users can choose to revise newly learned concepts with flashcards. Currently, there is a default deck of Greek gods. Users can add their own cards by using the form beneath.

New cards and the number of times users have visited each card are currently saved to the local storage of users’ browsers.

![Flashcard](img/flashcard.png)

**Consideration**

To replicate a real flashcard, we use flipping animation that occurs when users click on anywhere on the card.

Previously, we did not allow users to add cards to the card set while in learning mode. However, doing so may affect the user's workflow. Therefore, we came up with the current implementation.

### 12.2.5 Route protection

Unauthorized users can only access the Authentication and Registration system. Similarly, logged-in users can only view Dashboard, Calendar, Pomodoro Timer, and Flashcard before signing out.


# 13. Testing

Django provides a test framework with a hierarchy of classes that build on the Python standard unittest library. Django has a default test.py file for each application of the project. 

However, to cope with the complexity of the website and a large number of views and models created (and to be created), we write two separate files test_views.py and test_models.py, which are stored in the tests directory of each application instead.

## 13.1 View Testing

We want to ensure that the views of each application are handled correctly. To do that, test functions are written to check the template rendering, the HTTP status codes and assert the messages to the client. 

The testing functions are created under the `TestViews` class, which is inherited from the `TestCase` class of `django.test`. The test view functions include:

* Authentication view tests (implemented)
  * Register page
  * Login page
  * Should / should not sign up user
  * Should / should not login user
* Dashboard view tests (to be implemented before Milestone 2)
  * Home page
  * Calendar page
  * Pomodoro Timer page
  * Flashcards page

Details of the implemented tests are included in the table below.

(table)

## 13.2 Model Testing

The User class is inherited from the `AbstractUser` class of `django.contrib.auth.models`. The test function is written under the `TestModel` class (inherited from the `TestCase` class of `django.test`). It checks whether the user can be created correctly and asserts the matching of user information

```python
from authentication.models import User
from django.test import TestCase

class TestModel(TestCase):

    def test_should_create_user(self):
        user = User.objects.create_user(
                username='username', 
                email='email@app.com',
            )
        user.set_password('password123')
        user.save()

        self.assertEqual(str(user), 'email@app.com')
```

In the example above, the `test_should_create_user` creates a new testing user with `username = ‘username’` and `email = ‘email@app.com’`. Then, it then checks if this information is stored correctly in the database and its string representation is correct or not.

## 13.3 Running Tests

To run tests, run the command `$ python manage.py test`.

A test database will be created so that the main database will not be affected. The program will report the bugs detected, the run time, and the overall status. Finally, the test database will be destroyed.

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 1.157s

OK
Destroying test database for alias 'default'...
```

## 13.4 User Acceptance Testing

When the prototype for ActiveNUS is ready, acceptance testing will be conducted. The sample size for acceptance is projected to be 50, composed of our target users which are university students.

We intend to inquire testers on the following features:

**Authentication**
* Is it easy and intuitive to navigate to the registration page for new users?
* Is it easy and intuitive to log in for existing users?
* If the users fail to provide valid credentials on logging in, do users face any difficulties setting up a new password?

**Dashboard and to-do list**
* Is the user interface of the dashboard and to-do list clear and comprehensive on users’ tasks and progress?
* Do users face any inconveniences while viewing their progress boxes?
* Do users face any inconveniences to add, track and delete to-do list tasks?

**Calendar**
* Do users face any inconveniences to add, update and delete calendar events?
* Is it easy and intuitive for users to view different viewing modes of the calendar (monthly, weekly and daily view)?
* Do users face any other inconveniences while using the calendar?

**Pomodoro timer**
* Is it easy and intuitive for users to choose different modes of Pomodoro timer (focus mode, short break mode, long break mode)?
* What do users think of the notification? Is the volume suitable for a working/studying environment? 
* What do users think of the gamified reward scheme? Is it exciting enough to motivate users?

**Flashcard**
* Do users face any inconveniences when adding new cards and using existing card decks?
* Are the animation and user interface pleasant to use?
* Are the automatically recommended cards really the ones that users need to reinforce?


# 14. Software Security Measures

To ensure the safety of our database and the privacy of users, we introduced some security measures.

## 14.1 CSRF Token

A CSRF (Cross-site request forge) token is a unique, secret, unpredictable value generated by the server-side application and transmitted to the client so that it is included in a subsequent HTTP request made by the client. When the later request is made, the server-side application validates that the request consists of the expected token and rejects the request if the token is missing or invalid.

CSRF tokens can prevent CSRF attacks by making it impossible for an attacker to construct a fully valid HTTP request suitable for feeding to a victim user. Since the attacker cannot determine or predict the value of a user's CSRF token, they cannot construct a request with all the necessary parameters for the application to honor the request.

In ActiveNUS, POST requests are used in the registration system and other forms for users to add the information. Therefore, CSRF tokens are used to protect the database of unwanted threats.

## 14.2 Password Hashing

If the user's password is stored as plaintext in the database, the system can be put at risk by unwanted attacks. Moreover, user privacy may be violated if necessary practices are not taken. Therefore, we hash people's passwords using SHA265 algorithm with 260,000 iterations and salt added.

A hash is a ‘one-way’ cryptographic function, and the output of hashing has a fixed size for any size of the source text. A good hash function should map the expected inputs as evenly as possible over its output range. That is, every hash value in the output range should be generated with roughly the same probability. Also, a very small change of the input should lead to a significant variation of the output. 

We choose SHA256 to protect users’ passwords because it satisfies all properties of a good hash function as mentioned above. To enhance security, we run the hash function through 260,000 iterations with salt (adding random bits to each password instance before hashing).