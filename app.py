from flask import Flask

myapp = Flask(__name__)

profiles = [
    {
        "id" : 1,
        "name" : "sachi vania"
    }, 
    {
        "id" : 2,
        "name" : "nemi upadhyay"
    }, 
    {
        "id" : 3,
        "name" : "demo user"
    }
]

# get all users
@myapp.route('/users')
def getAllUsers():
    pass

# get user by id
@myapp.route('/users/<int:id>')
def getUserById():
    pass

# create user
@myapp.route('/users')
def createUser():
    pass

# update user
@myapp.route('/users/<int:id>')
def updateUser():
    pass

# delete user
@myapp.route('/users/<int:id>')
def deleteUser():
    pass

if __name__ == '__main__':
    myapp.run(debug=True)