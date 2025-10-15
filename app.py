from flask import Flask

""" __name__ means name of this module ('app'.py) i.e. 'app' """
myapp = Flask(__name__)

""" 
The route() function of the Flask class is a decorator, 
which tells the application which URL should call 
the associated function. 
"""
@myapp.route('/')
def homepage():
    return 'Welcome to the intial flask app!'

if __name__ == '__main__':
    # run the app on the local development server
    myapp.run(debug=True)
    """ to reload the app on code change, keep debug = True """

    """
    Be default the flask app runs on localhost and on port = 5000.
    To change the host and/or port,
    myapp.run(host="0.0.0.0", port=5001)
    This is useful when we want to give a custom static ip to our flask app
    (Assuming this ip is not already being used)
    """