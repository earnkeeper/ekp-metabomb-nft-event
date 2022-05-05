import eventlet
import eventlet.wsgi
import socketio
from decouple import config
from flask import Flask, send_from_directory
from flask_cors import CORS, cross_origin
import json
import time

PLUGIN_ID = config("EKP_PLUGIN_ID", default="developer-mode")
PORT = config("PORT", default=3001, cast=int)

class ClientService:
    def __init__(self, controllers):
        for controller in controllers:
            controller.client_service = self
        self.controllers = controllers

        self.sio = self.__get_socket_io()
        self.app = self.__get_web_app()
        self.app.wsgi_app = socketio.WSGIApp(self.sio, self.app.wsgi_app)

    def __get_socket_io(self):
        sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*')

        @sio.event
        def connect(sid, environ, auth):
            for controller in self.controllers:
                controller.on_connect(sid)

        @sio.on('client-state-changed')
        def on_client_state_changed(sid, data):
            for controller in self.controllers:
                controller.on_client_state_changed(sid, json.loads(data))

        return sio

    def __get_web_app(self):
        app = Flask("__main__")
        CORS(app)
        app.config['CORS_HEADERS'] = 'Content-Type'

        @app.route('/static/<path:path>')
        @cross_origin
        def meta(path):
            return send_from_directory("static", path)

        return app

    def listen(self):
        eventlet.wsgi.server(eventlet.listen(('', PORT)), self.app)

    def add_controller(self, controller):
        self.controllers.append(controller)


    def emit_busy(self, sid, collection_name):
        layer = {
            "id": f"busy-{collection_name}",
            "collectionName": "busy",
            "set": [{"id": collection_name, }],
            "timestamp": int(time.time())
        }
        self.emit_add_layers(sid, [layer])

    def emit_done(self, sid, collection_name):
        message = {
            "query": {
                "id": f'busy-{collection_name}',
            }
        }
        self.sio.emit('remove-layers', json.dumps(message), room=sid)

    def emit_menu(self, sid, icon, title, nav_link):
        """
        Sends menu layer from server to the client side
        """

        layer = {
            "id": f"{PLUGIN_ID}_menu_{nav_link}",
            "collectionName": "menus",
            "set": [
                {
                    "id": f"{PLUGIN_ID}_{nav_link}",
                    "icon": icon,
                    "title": title,
                    "navLink": nav_link,
                }
            ],
            "timestamp": int(time.time())
        }

        self.emit_add_layers(sid, [layer])

    def emit_page(self, sid, path, element):
        """
        Sends main page content from server to the client side
        """

        layer = {
            "id": f"{PLUGIN_ID}_page_{path}",
            "collectionName": "pages",
            "set": [
                {
                    "id": path,
                    "element": element
                }
            ],
            "timestamp": int(time.time())
        }

        self.emit_add_layers(sid, [layer])

    def emit_documents(self, sid, collection_name, documents):

        layer = {
            "id": f"{PLUGIN_ID}_{collection_name}",
            "collectionName": collection_name,
            "set": documents,
            "timestamp": int(time.time())
        }

        message = {
            "layers": [
                {
                    "id": collection_name,
                    "collectionName": collection_name,
                    "set": documents,
                    "timestamp": int(time.time())
                }
            ]
        }

        self.emit_add_layers(sid, [layer])

    def emit_add_layers(self, sid, layers):
        message = {
            "layers": layers
        }
        self.sio.emit('add-layers', json.dumps(message), room=sid)