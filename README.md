# ActiveNUS

[![Django CI](https://github.com/nvbinh15/ActiveNUS/actions/workflows/django.yml/badge.svg?branch=main)](https://github.com/nvbinh15/ActiveNUS/actions/workflows/django.yml)

## Description
This repo contains our source code for ActiveNUS - a web-based application for the CP2106 (Independent Software Development Project) module at NUS.

For more details, please refer to our [documentation](https://nvbinh15.github.io/ActiveNUS/).

## Deployment
ActiveNUS is deployed on Railway platform and works well on most web browsers and devices. You can use our product at [activenus.up.railway.app](https://activenus.up.railway.app/). You should use desktop/laptop for the best experience.

If you are using Safari, please update to the latest version.

## Set Up Instruction

Clone the codebase and install all the required packages by running `$ pip install -r requirements.txt` (you may want to use a Python virtual environment to isolate all the dependencies).

Create a new file `.env` in the current directory that stores all the environment information. Type in your secret key (Django secret key), your email address, and your email password. The content of the file should be like this:

```
export SECRET_KEY=’<YOUR_SECRET_KEY>’
export EMAIL_FROM_USER=<YOUR_EMAIL_ADDRESS>
export EMAIL_HOST_PASSWORD=<YOUR_EMAIL_PASSWORD>
```

Activate the `.env` file by running `$ source .env`

> Now, everything is set up. You can run the website locally by `$ python3 manage.py runserver`. The local server deployment should be found at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Running Tests

To run tests, use the command `$ python3 manage.py test`.

A test database will be created so that the main database will not be affected. The program will report the bugs detected, the run time, and the overall status. Finally, the test database will be destroyed.
