from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')
db = client['github_events']

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    db.events.insert_one(data)
    return jsonify({'message': 'Event received successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
