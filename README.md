# Overview
This program is designed to demonstrate how to build a basic web app using Django, as well as learning how to write html files.

I built a basic mad-libs app that allows the user to choose one word they would like to insert into a story.\
To start the server on your computer, find what folder the program is stored in\
and run "source (path to Django_web_app folder)/second_django/bin/activate".\
Then change directories to second_django/mysite2,\
make sure you have django installed with "pip install django", and run "python3 manage.py runserver".\
To get to the first page of the website, go to "http://127.0.0.1:8000/madlibs" in your web browser.

[You are watching this now](https://youtu.be/7KHJHPEdCpQ)

# Web Pages
"madlibs/" is the index page that lists all available stories.\
This page dynamically creates a link to each stories' input page with the name of the story as the text.\
"madlibs/1/input" is the input page for story 1. \
This page dynamically creates a header with the story name and a list of word choices for the user.\
"madlibs/1/results" is the results page.\
This page dynamically creates a story with the selected word from the input page in the story.\
This page also creates a dynamic link to the input page of the currently selected story.
# Development Environment

* Django 3.2.1
* Visual Studios Code
* Python 3.8
* HTML

# Useful Websites

* [Create first web app with Django](https://docs.djangoproject.com/en/3.2/contents/)
* [Django API](https://docs.djangoproject.com/en/3.2/intro/tutorial02/#playing-with-the-api)

# Future Work

* Item 1: Allow the user to enter their own text instead of using a radio button selection system.
* Item 2: Add more stories.
* Item 3: Fix no-input warning.
* Item 4: Add images or backgrounds.