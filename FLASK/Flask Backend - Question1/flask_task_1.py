# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    if 'numbers' in data and isinstance(data['numbers'], list):
        try:
            result = sum(data['numbers'])
            return jsonify({'sum': result})
        except TypeError:
            return jsonify({'error': 'Invalid input. Numbers must be integers.'}), 400
    else:
        return jsonify({'error': 'Invalid input. Please provide a list of numbers.'}), 400

@app.route('/concatenate', methods=['POST'])
def concatenate_strings():
    data = request.get_json()
    if 'strings' in data and isinstance(data['strings'], list) and len(data['strings']) == 2:
        try:
            result = ''.join(data['strings'])
            return jsonify({'concatenated_string': result})
        except TypeError:
            return jsonify({'error': 'Invalid input. Strings must be valid strings.'}), 400
    else:
        return jsonify({'error': 'Invalid input. Please provide a list of two strings.'}), 400

if __name__ == '__main__':
    app.run()
