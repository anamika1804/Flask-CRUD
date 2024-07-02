from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify, request

from pymongo import MongoClient

from werkzeug.security import generate_password_hash, check_password_hash


app= Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb+srv://anamikaktm:n3bwQrpOdPrrzcJc@users.umsmqu3.mongodb.net/Users"

mongo =PyMongo(app)

@app.route('/add', methods = ['POST'])
def add_user():
    try: 
        _json = request.json
        _name =_json['name']
        _email = _json['email']
        _password=_json['password']

        print(f"Received data: name={_name}, email={_email}, password={_password}")

        if _name and _email and _password and  request.method == 'POST':
            _hashed_password = generate_password_hash(_password)

            id = mongo.db.user.insert_one({'name': _name, 'email':_email, 'password': _hashed_password})
            
            if id.inserted_id:
                resp = jsonify("User added successfully")

                resp.status_code = 200

                print("User added successfully")

                return resp
            else:
                return jsonify({"error":"Failed to add user"}), 500
        
        else :
            return not_found()
        
    except Exception as e:
        # Debug print statement
        print(f"Error: {e}")
        return jsonify(str(e)), 500
    
@app.route('/users')
def users():
    users = mongo.db.user.find()
    resp = dumps(users)
    return resp


@app.route('/user/<id>')
def user(id):
    user = mongo.db.user.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp

@app.route('/delete/<id>', methods = ['DELETE'])
def delete_user(id):
    mongo.db.user.delete_one({'_id': ObjectId(id)})
    resp = jsonify("User deleted succesfully")


    resp.status_code= 200

    return resp

@app.route('/update/<id>', methods = ['PUT'])
def update_user(id):
    _id=id
    _json= request.json
    _name = _json ['name']
    _email = _json['email']
    _password= _json['password']


    if _name and _email and _password and _id and request.method == 'PUT':
        _hashed_password = generate_password_hash(_password)

        mongo.db.user.update_one({'_id': ObjectId(_id['$oid'])if '$oid' in _id else ObjectId(_id)}, {'$set': {'name': _name, 'email': _email, 'password': _hashed_password}})

        resp = jsonify("User updated successfully")

        resp.status_code = 200

        return resp
    
    else:
        return not_found()
    





@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message':'Not found'+ request.url
    }

    resp = jsonify(message)

    resp.status_code= 404

    return resp
    

if __name__ == "__main__":
    app.run(debug=True)
    
