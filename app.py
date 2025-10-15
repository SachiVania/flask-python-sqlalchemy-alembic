from flask import Flask

# __name__ means name of this module ('app'.py) i.e. 'app'
myapp = Flask(__name__)

# Binding URL and function together
@myapp.route('/')
def homepage():
    return 'Welcome to the intial flask app!'

if __name__ == '__main__':
    # run the app
    # to reload the app on code change, keep debug = True
    myapp.run(debug=True)

    """
    Be default the flask app runs on localhost and on port = 5000.
    To change the host and/or port,
    myapp.run(host="0.0.0.0", port=5001)
    """