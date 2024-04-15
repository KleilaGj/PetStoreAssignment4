from flask import Flask, jsonify, request
# Code to intergrate flask aplication with database utilities 
from db_utils import connect_to_database, execute_query
app = Flask(__name__)
# initialize database connection 
db_connection = connect_to_database()
# defne a route to retrieve all pets from the database 
@app.route('/pets', methods=['GET'])
def get_pets():
    # construct a SQL query to select all pets from the database 
    query = "SELECT * FROM Pets_info"
    # Execute the SQL query and retrieve pets data 
    pets = execute_query(db_connection, query)
    # Return JSON response containing pets data 
    return jsonify(pets)
# Modified route to support both GET and PUT methods
@app.route('/pets/<int:pet_id>', methods=['GET', 'PUT'])
def get_or_update_pet(pet_id):
    if request.method == 'GET':
        # SELECT query to fetch a specific pet by ID
        query = "SELECT * FROM Pets_info WHERE pet_id = %s"
        # provide the pet ID as data for the query
        data = (pet_id,)
        #Execute the SQL query and retrieve the pet data 
        pet = execute_query(db_connection, query, data)
        # check if the pet exists and return JSON response accordingly 
        if pet:
            return jsonify(pet)
        else:
            return jsonify({"message": "Pet not found"}), 404
    elif request.method == 'PUT':
        # retieve JSON data from the request body 
        data = request.get_json()
        # Extract information for updating the pet 
        new_name = data.get('name')
        new_breed = data.get('breed')
        new_age = data.get('age')
        new_price = data.get('price')

        # UPDATE query to modify pet's information in the database
        update_query = "UPDATE Pets_info SET name=%s, breed=%s, age=%s, price=%s WHERE pet_id=%s"
        update_data = (new_name, new_breed, new_age, new_price, pet_id)
        #Execute the SQL query to update the pet's information 
        execute_query(db_connection, update_query, update_data)
        
        #return JSON response indicating successful updating 
        return jsonify({"message": "Pet information updated successfully"}), 200
#define a function to start the Flask application with a welcome statement 
def run():
    print("Welcome to the Pet Store API!")
    app.run(debug=True)
    #check if the script is executed directly
if __name__ == '__main__':
    # call the run function to start the Flask application 
    run()
    

