"""
This file contains the API endpoints for real time chat.
"""

from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/chat', methods=['GET'])
def chat():
    """
    Chat page.
    :return:
    chat page
    """
    return render_template('index.html', host='http://127.0.0.1:5000')


@socketio.on('message')
def send_message(data):
    """
    Send a message to the chat.
    :param data:
    message data
    :return:
    None
    """
    print(f"Message: {data}")
    socketio.emit('receive_message', data)


@socketio.on('connect')
def handle_connect():
    print('Client connected to the server')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected from the server')


if __name__ == '__main__':
    socketio.run(app, debug=True)
