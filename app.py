from flask_socketio import SocketIO
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
sio = SocketIO(app)

#sio = socketio.Server()
#app = Flask(__name__)


@app.route('/')
def index():
    """Serve the client-side application."""
    return "Server ROOT DIR"

@sio.on('join')
def join(Nickname):

    sio.emit('userjoinedthechat',Nickname +" : has joined the chat ",broadcast=True)



@sio.on('messagedetection', namespace='/')
def messagedetection(Nickname, msg):

    msg = {"message":msg, "senderNickname":Nickname}

    print(Nickname + " : " + str(msg))

    sio.emit('message', msg ,broadcast=True)




@sio.on('disconnect')
def disconnect():
	sio.emit("userdisconnect"," user has left ",broadcast=True) 



if __name__ == '__main__':
   # socketio.run(app)

    sio.run(app,debug=True)
    # wrap Flask application with engineio's middleware
   # app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    #eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
