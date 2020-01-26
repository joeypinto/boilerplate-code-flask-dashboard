# Flask Dashboard [Boilerplate Code](https://appseed.us/boilerplate-code)

Playground **boilerplate code** used by the **[AppSeed](https://appseed.us)** community for simple [Flask Admin Dashboards](https://appseed.us/admin-dashboards/flask).

<br />

## How it works

Anyone can submit requests for new modules and features using the issues tracker provided by Github. Popular features will be coded by the AppSeed team and later integrated in the automated workflow. 
For more information please access the **[AppSeed](https://appseed.us)** platform or join the community on [Discord](https://discord.gg/fZC6hup). 

<br />

## Features

- UI-ready, MIT License
- SQLite, PostgreSQL, SQLAlchemy ORM
- Alembic (for DB schema migrations)
- Modular design with **Blueprints**
- Session-Based authentication (via **flask_login**)
- Forms validation
- Deployment scripts: Docker, Gunicorn
- Session-Based authentication flow (login, register)

<br/>

## Sample Apps

A short-list with web apps that use this simple boilerplate:

- [Flask Dashboard Argon](https://github.com/app-generator/flask-boilerplate-dashboard-argon)
- [Flask Dashboard Material](https://github.com/app-generator/flask-material-dashboard)
- [Flask Dashboard Black](https://github.com/app-generator/flask-black-dashboard)

<br />

## New Features

- How to submit a feature request

The new features, will be opened as issues labeled as enhancements and voted by the community.

- How to test a new feature

Fork the project, create a new branch and code the new module / feature  

<br />

## Help & Support

- Via eMail < [support @ appseed.us](https://appseed.us/support) > and **Github** issues tracker
- LIVE Support via [Discord](https://discord.gg/fZC6hup)

## Build from sources

```bash
$ # Get the code
$ git clone https://github.com/app-generator/boilerplate-code-flask-dashboard.git
$ cd boilerplate-code-flask-dashboard
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv --no-site-packages env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv --no-site-packages env
$ # .\env\Scripts\activate
$ 
$ # Install modules
$ # SQLIte version (no PostgreSQL)
$ pip3 install -r requirements-sqlite.txt
$ 
$ # OR with PostgreSQL connector
$ pip install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000s
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```

If all goes well, we should see the app running in the browser.
> Note: to pass the login, and unlock the private pages, please create a new user (via register page) and after, authenticate using the login page.

![Flask Dashboard Argon - Open-Source Admin Panel.](https://raw.githubusercontent.com/app-generator/static/master/products/flask-boilerplate-dashboard-argon-screen.png)

<br />

## Docker execution

The application can be easily excuted in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/app-generator/boilerplate-code-flask-dashboard.git
$ cd boilerplate-code-flask-dashboard
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:5000` in your browser. The app should be up & running.

<br />

---
Flask Dashboard [Boilerplate Code](https://appseed.us/boilerplate-code) - Provided by **AppSeed - [Web App Generator](https://appseed.us/app-generator)**.
