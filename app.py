from flask import Flask, jsonify, request

myapp = Flask(__name__)

profiles = [
    {"id" : 1,"name" : "sachi vania"}, 
    {"id" : 2,"name" : "nemi upadhyay"}, 
    {"id" : 3,"name" : "demo user"}
]

# get all users
@myapp.route('/users', methods=['GET'])
def getAllUsers():
    return jsonify(profiles)

# get user by id
@myapp.route('/users/<int:id>', methods=['GET'])
def getUserById(id):
    for profile in profiles:
        if profile['id'] == id: 
            break
    else:
        return jsonify('profile not found')
    
    # another way of writing the above code
    # profile = next((profile for profile in profiles if profile['id'] == id), None)
    # if not profile:
    #   return jsonify('profile not found')

    return jsonify(profile)

# create user
@myapp.route('/users', methods=['POST'])
def createUser():
    new_profile = request.json
    profiles.append(new_profile)
    return jsonify("profile added successfully")

# update user
@myapp.route('/users/<int:id>', methods=['PUT'])
def updateUser(id):
    profile = next((profile for profile in profiles if profile['id'] == id), None)
    if not profile:
        return jsonify('profile not found. update failed.')

    updated_profile = request.json

    # get index of the profile to be updated.
    index = next((i for i, profile in enumerate(profiles) if profile['id'] == id), None)
    if index is None:
        return jsonify('index not found. update failed.')

    # update the record
    profiles.insert(index, updated_profile)
    return jsonify('profile updated successfully')

# delete user
@myapp.route('/users/<int:id>', methods=['DELETE'])
def deleteUser(id):
    profile = next((profile for profile in profiles if profile['id'] == id), None)
    if not profile:
        return jsonify('profile not found. delete failed.')

    # get index of the profile to be updated.
    index = next((i for i, profile in enumerate(profiles) if profile['id'] == id), None)
    if index is None:
        return jsonify('index not found. delete failed.')

    profiles.remove(profile)
    return jsonify('profile deleted successfully')

if __name__ == '__main__':
    myapp.run(debug=True)