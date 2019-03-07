import bottle
import json
import Server.players


@bottle.route('/')
def get_index():
    return bottle.static_file("index.html", root="")


@bottle.post('join')
def set_name():
    content = bottle.request.body.read().decode()
    content = json.loads(content)
    Server.players.add_name(content['message'])
    return json.dumps(Server.players.store_name())


@bottle.error("404")
def meme_error():
    return "Mission failed, we'll get em next time boys"


bottle.run(host="localhost", port=8080, debug=True)
