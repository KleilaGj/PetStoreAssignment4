from flask import Flask, jsonify, request

app = Flask(__name__)

pets = [
    {"id": 1, "name": "Dog", "breed": "Poodle", "age": 2, "price": 500},
    {"id": 2, "name": "Cat", "breed": "Ginger", "age": 3, "price": 300},
    {"id": 3, "name": "Bird", "breed": "Parrot", "age": 1, "price": 200}
]

orders = []


@app.route('/pets', methods=['GET'])
def get_pets():
    return jsonify(pets)

@app.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    pet = next((pet for pet in pets if pet['id'] == pet_id), None)
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
    pet = next((pet for pet in pets if pet['id'] == pet_id), None)
    if not pet:
        return jsonify({"message": "Pet not found"}), 404
    orders.append({"pet_id": pet_id})
    return jsonify({"message": "Order placed"}), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((order for order in orders if order['id'] == order_id), None)
    if order:
        return jsonify(order)
    else:
        return jsonify({"message": "Order not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
