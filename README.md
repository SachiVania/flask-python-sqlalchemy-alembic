# flask-python-sqlalchemy-alembic

### In WSL
### Download python3.10
```
$ python3 --version
Python 3.10.12
```

### Create a virtual environment
```
$ cd myproject

# install the virtualenv, if not done
$ pip install virtualenv

# create the virtual environment (only the first time)
# note: 'python3 -m venv venv' command gets stuck in wsl
$ virtualenv venv

# activate the virtual env
$ source venv/bin/activate
```

### Install dependecies
```
$ pip install flask
$ pip freeze > requirements.txt
```
Note: it takes time to install the dependencies in WSL

### Run the app
```
# To run the flask app on localhost and with default 5000 port
$ python3 app.py
or
$ flask --app app run

# To run the flask app on other port, accessible by other machines in the same network
$ set FLASK_APP=app.py
$ flask run --host=192.168.15.23 --port=5001
```