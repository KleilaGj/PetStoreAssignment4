from flask import Flask, jsonify, request
#adding new code to intergrate flask aplication with database utilities 
from db_utils import connect_to_database, execute_query
app = Flask(__name__)
#adding code to connect to the database 
db_connection = connect_to_database()
# previous code pets = [
    {"id": 1, "name": "Dog", "breed": "Poodle", "age": 2, "price": 500},
    {"id": 2, "name": "Cat", "breed": "Ginger", "age": 3, "price": 300},
    {"id": 3, "name": "Bird", "breed": "Parrot", "age": 1, "price": 200}
]

#previous code orders = []

#modifiying current code 
@app.route('/pets', methods=['GET'])
def get_pets():
    #getting pets data from database 
    query = "SELECT * FROM Pets_info"
    pets = execute_query(db_connection, query)
    return jsonify(pets)
#modifying code 
@app.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    query = "SELECT * FROM Pets_info WHERE pet_id = %s"
    data = (pet_id,)
    if pet:
        return jsonify(pet)
    else:
        return jsonify({"message": "Pet not found"}), 404

@app.route('/orders', methods=['POST'])
def place_order():
    data = request.get_json()
    pet_id = data.get('pet_id')
    if not pet_id:
        return jsonify({"message": "Pet ID is required"}), 400
        #check if the pet exists in the database 
query =  "SELECT * FROM Pets_info WHERE pet_id = %s"
pet_data = (pet_id,)
pet = execute_query(db_connection, query, pet_data)
    if not pet:
        return jsonify({"message": "Pet not found"}), 404
#insert order into the database 
query = "INSERT INTO Orders (pet_id) VALUES (%s)"
    order_data = (pet_id,)
    execute_query(db_connection, query, order_data)
    return jsonify({"message": "Order placed"}), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    # Fetch order data by ID from the database
    query = "SELECT * FROM Orders WHERE order_id = %s"
    data = (order_id,)
    order = execute_query(db_connection, query, data)
    if order:
        return jsonify(order)
    else:
        return jsonify({"message": "Order not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
