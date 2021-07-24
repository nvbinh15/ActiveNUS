# ActiveNUS

[![Django CI](https://github.com/nvbinh15/ActiveNUS/actions/workflows/django.yml/badge.svg?branch=main)](https://github.com/nvbinh15/ActiveNUS/actions/workflows/django.yml)

## Description
This repo contains our source code for ActiveNUS - a web-based application for the CP2106 (Independent Software Development Project) module at NUS.

For more details, please refer to our [documentation](https://nvbinh15.github.io/ActiveNUS/).

## Deployment
ActiveNUS is deployed on Heroku platform. You can use our product at [activenus.herokuapp.com](https://activenus.herokuapp.com/)

## Set Up Instruction

Change into the directory you want to store the code (the directory must not contain any non-empty directory named `ActiveNUS`).

Clone the codebase by `$ git clone https://github.com/nvbinh15/ActiveNUS.git`

A new `ActiveNUS` directory will be created in the current directory.

Change into the `ActiveNUS` directory.

Create a virtual environment with `python3` by running `$ virtualenv -p python3 venv`. A new directory called `venv` will be created in the current directory.

Activate the `venv` environment by running `$ source venv/bin/activate`. You are now switching to the `venv` environment.

Install all the required packages by running `$ pip install -r requirements.txt`

Create a new file `.env` in the current directory that stores all the environment information. Type in your secret key (django secret key), your email address, and your email password. The content of the file should be like this:

```
export SECRET_KEY=’<YOUR_SECRET_KEY>’
export EMAIL_FROM_USER=<YOUR_EMAIL_ADDRESS>
export EMAIL_HOST_PASSWORD=<YOUR_EMAIL_PASSWORD>
```

Activate the `.env` file by running `$ source .env`

Now, everything is set up. You can run the website locally by `$ python manage.py runserver`. The local server deployment should be found at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Running Tests

To run tests, run `$ python manage.py test`.

A test database will be created so that the main database will not be affected. The program will report the bugs detected, the run time, and the overall status. Finally, the test database will be destroyed.