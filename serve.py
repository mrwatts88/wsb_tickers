from flask import Flask
from aggregator import Aggregator
import asyncio
import websockets
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
from reddit_client import RedditClient

PERIOD = 5
TOP = 50

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)
aggregator = Aggregator(PERIOD, TOP)
client = RedditClient(aggregator, socketio)
client.start_streaming()

@socketio.on('test')
def handle_message(data):
    emit("res", "from the server")

if __name__ == '__main__':
    socketio.run(app)
