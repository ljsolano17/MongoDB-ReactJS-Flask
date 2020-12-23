from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonreactdb'
mongo = PyMongo(app)

CORS(app)#para comunicarse con el servidor y no de problemas con react

db = mongo.db.users
db2 = mongo.db.pacientes

@app.route('/users', methods=['POST'])
#CREATE
def createUser():
   
    id = db.insert({
        'name':request.json['name'],
        'email':request.json['email'],
        'password':request.json['password']
    })
    #print(str(ObjectId(id)))
    return jsonify(str(ObjectId(id)))

@app.route('/users', methods=['GET'])
#READ
def getUsers():
    users = []
    
    for item in db.find():
        users.append({
            '_id':str(ObjectId(item['_id'])),
            'name':item['name'],
            'email':item['email'],
            'password':item['password']
            
        })
    return jsonify(users)

@app.route('/user/<id>', methods=['GET'])
#READ ONE
def getUser(id):
    user = db.find_one({'_id':ObjectId(id)})
    return jsonify({
        '_id':str(ObjectId(user['_id'])),
        'name':user['name'],
        'email':user['email'],
        'password':user['password']
    })

@app.route('/users/<id>', methods=['DELETE'])
#DELETE
def deleteUser(id):

    db.delete_one({'_id':ObjectId(id)})

    print(id)
    return jsonify({'Message':"User Deleted"})

@app.route('/users/<id>', methods=['PUT'])
#UPDATE
def updateUser(id):
    print(id)
    print(request.json)
    db.update_one({'_id':ObjectId(id)}, {'$set': {
        'name':request.json['name'],
        'email':request.json['email'],
        'password':request.json['password']
    }})
    return jsonify({'Message':"User Updated"})

 

@app.route('/pacientes', methods=['POST'])
#CREATE
def createPaciente():
   
    id = db2.insert({
        'nombre':request.json['nombre'],
        'email':request.json['email'],
        'cedula':request.json['cedula']
    })
    #print(str(ObjectId(id)))
   # return jsonify(str(ObjectId(id)))
    return jsonify(str(ObjectId(id)))


@app.route('/pacientes', methods=['GET'])
#READ
def getPacientes():
    pacientes = []
    
    for item in db2.find():
        pacientes.append({
            '_id':str(ObjectId(item['_id'])),
            'nombre':item['nombre'],
            'email':item['email'],
            'cedula':item['cedula']
            
        })
    return jsonify(pacientes)


if __name__ == "__main__":
    app.run(debug = True)























