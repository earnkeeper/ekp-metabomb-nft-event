
from features.boxes.controller import on_client_state_changed_boxes
import json
import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, send_from_directory
from flask_cors import CORS, cross_origin

PORT = 3001

sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*')
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

@app.route('/static/<path:path>')
@cross_origin
def meta(path):
    return send_from_directory("static", path)


@sio.on('client-state-changed')
def on_event(sid, data):
    on_client_state_changed_boxes(sio, sid, json.loads(data))


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', PORT)), app)
