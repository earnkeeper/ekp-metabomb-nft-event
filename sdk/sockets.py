import json
import time


def emit_menu(sio, sid, id, title, nav_link, icon):
    menu = {
        "id": id,
        "title": title,
        "navLink": nav_link,
        "icon": icon
    }
    message = {
        "layers": [
            {
                "id": "menu-%s" % (id),
                "collectionName": "menus",
                "set": [menu],
                "timestamp": int(time.time())
            }
        ]
    }
    sio.emit('add-layers', json.dumps(message), room=sid)


def emit_page(sio, sid, id, element):
    page = {
        "id": id,
        "element": element
    }
    message = {
        "layers": [
            {
                "id": f'page-{id}',
                "collectionName": "pages",
                "set": [page],
                "timestamp": int(time.time())
            }
        ]
    }
    sio.emit('add-layers', json.dumps(message), room=sid)


def emit_busy(sio, sid, collection_name):
    message = {
        "layers": [
            {
                "id": f'busy-{collection_name}',
                "collectionName": "busy",
                "set": [{"id": collection_name}],
                "timestamp": int(time.time())
            }
        ]
    }
    sio.emit('add-layers', json.dumps(message), room=sid)


def emit_done(sio, sid, collection_name):
    message = {
        "query": {
            "id": f'busy-{collection_name}',
        }
    }
    sio.emit('remove-layers', json.dumps(message), room=sid)


def emit_documents(sio, sid, collection_name, documents):
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
    sio.emit('add-layers', json.dumps(message), room=sid)
