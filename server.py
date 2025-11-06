from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def handle_data():
    # Assuming the need for a JSON input
    data = request.get_json()
    # Process the data here
    # For now, just return what was received
    return jsonify({'received': data}), 200

if __name__ == '__main__':
    app.run(debug=True)