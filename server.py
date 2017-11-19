from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socket = SocketIO(app)

with open('file.txt', 'w') as f:
    f.write(str(0))

def read_file(file, change):
    with open(file, 'r') as f:
        value = int(f.read()) + int(change)
    with open(file, 'w') as f:
        f.write(str(value))
    return value

@socket.on('refresh')
def refresh(change):
    socket.emit('value', read_file('file.txt', change))

if __name__ == '__main__':
    socket.run(app,host= '0.0.0.0')
