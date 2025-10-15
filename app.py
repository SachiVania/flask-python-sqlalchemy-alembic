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
@myapp.route('/users', methods=['GET'])
def getAllUsers():
    pass

# get user by id
@myapp.route('/users/<int:id>', methods=['GET'])
def getUserById(id):
    return 

# create user
@myapp.route('/users', methods=['POST'])
def createUser():
    pass

# update user
@myapp.route('/users/<int:id>', methods=['PUT'])
def updateUser(id):
    pass

# delete user
@myapp.route('/users/<int:id>', methods=['DELETE'])
def deleteUser(id):
    pass

if __name__ == '__main__':
    myapp.run(debug=True)