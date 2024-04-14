from flask import Flask, jsonify, request

app = Flask(__name__)

pets = [
    {"id": 1, "name": "Dog", "breed": "Poodle", "age": 2},
    {"id": 2, "name": "Cat", "breed": "Ginger", "age": 3},
    {"id": 3, "name": "Bird", "breed": "Parrot", "age": 1}
]

orders = []


@app.route('/pets', methods=['GET'])
def get_pets():
    return jsonify(pets)


