from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

rooms = {}

@app.route('/')
def index():
    return render_template('index.html')

# JOIN ROOM + LOAD SAVED CODE
@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)

    try:
        with open(f"{room}.txt", "r") as f:
            rooms[room] = f.read()
    except:
        rooms[room] = ""

    emit('update_code', rooms[room], room=room)

# REAL-TIME UPDATE + SAVE CODE
@socketio.on('code_change')
def handle_code_change(data):
    room = data['room']
    code = data['code']

    rooms[room] = code

    # SAVE FILE
    with open(f"{room}.txt", "w") as f:
        f.write(code)

    emit('update_code', code, room=room, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True)
