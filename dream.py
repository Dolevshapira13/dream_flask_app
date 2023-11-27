from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hi there!'


@app.route('/json')
def get_json():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    return jsonify(response.json())


@app.route('/json/user/<int:user_id>', methods=['GET'])
def get_user_data(user_id):
    user_data_url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(user_data_url)
    tasks_data = response.json()

    user_tasks = [task for task in tasks_data if task["userId"] == user_id]

    if user_tasks:
        return jsonify(user_tasks)
    else:
        return jsonify({'error': f'User with userId {user_id} not found or has no tasks'}), 404


if __name__ == '__main__':
    app.run()
