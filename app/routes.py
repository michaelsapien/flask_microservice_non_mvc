from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/test', methods=['GET'])
def ping():
    return jsonify({"message": "success"}), 200
