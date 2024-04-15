from flask import Flask, jsonify, request
#adding new code to intergrate flask aplication with database utilities 
from db_utils import connect_to_database, execute_query
app = Flask(__name__)
#adding code to connect to the database 
db_connection = connect_to_database()
#modifiying current code 
@app.route('/pets', methods=['GET'])
def get_pets():
    #getting pets data from database 
    query = "SELECT * FROM Pets_info"
    pets = execute_query(db_connection, query)
    return jsonify(pets)
# Modified route to support both GET and PUT methods
@app.route('/pets/<int:pet_id>', methods=['GET', 'PUT'])
def get_or_update_pet(pet_id):
    if request.method == 'GET':
        # SELECT query to fetch a specific pet by ID
        query = "SELECT * FROM Pets_info WHERE pet_id = %s"
        data = (pet_id,)
        pet = execute_query(db_connection, query, data)
        if pet:
            return jsonify(pet)
        else:
            return jsonify({"message": "Pet not found"}), 404
    elif request.method == 'PUT':
        # Update pet information
        data = request.get_json()
        new_name = data.get('name')
        new_breed = data.get('breed')
        new_age = data.get('age')
        new_price = data.get('price')

        # UPDATE query to modify pet's information in the database
        update_query = "UPDATE Pets_info SET name=%s, breed=%s, age=%s, price=%s WHERE pet_id=%s"
        update_data = (new_name, new_breed, new_age, new_price, pet_id)
        execute_query(db_connection, update_query, update_data)

        return jsonify({"message": "Pet information updated successfully"}), 200
#define a function to start the Flask application with a welcome statement 
def run():
    print("Welcome to the Pet Store API!")
    app.run(debug=True)
if __name__ == '__main__':
    

