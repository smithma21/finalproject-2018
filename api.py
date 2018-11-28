from flask import Flask, request, make_response, json, url_for, abort
from db import Db
import string
import random

#Set Up
app = Flask(__name__)
db = Db()
app.debug = True
app.url_map.strict_slashes = False

#Error Codes

@app.errorhandler(500)
def server_error(e):
   return make_json_response({ 'error': 'unexpected server error' }, 500)

@app.errorhandler(404)
def not_found(e):
   return make_json_response({ 'error': e.description }, 404)

@app.errorhandler(403)
def forbidden(e):
   return make_json_response({ 'error': e.description }, 403)

@app.errorhandler(400)
def client_error(e):
   return make_json_response({ 'error': e.description }, 400)

#Routes

@app.route('/', methods = ['GET'])
def all_players():
    players = db.getPlayers()
    players_dict = {}
    for player in players:
       if 'player' in players_dict:
          players_dict['player'].append({'link' : '/' + player.username , 'firstname' : player.firstname, 'lastname' : player.lastname})
       else:
           players_dict['player'] = [{'link' : '/' + player.username ,'firstname' : player.firstname, 'lastname' : player.lastname}]
    return make_json_response(players_dict, 200)

@app.route('/<username>', methods = ['GET'])
def bucket_contents(username):
    pass

@app.route('/<username>', methods = ['PUT'])
def new_player(username):
    pass

@app.route('/<username>', methods = ['DELETE'])
def delete_player(username):
    pass

@app.route('/<bucketId>/', methods = ['GET'])
def get_all_games(username):
    pass

@app.route('/<username>/<gameID>', methods = ['GET'])
def get_game(username, gameID):
    pass

@app.route('/<username>', methods = ['POST'])
def create_game(username):
    pass

@app.route('/<username>/<gameID>', methods = ['DELETE'])
def delete_game(username, gameID):
    pass

# Starts the application
if __name__ == "__main__":
   app.run()

#Helper Function(s)
def makeId():
   return ''.join([random.choice(alphabet) for _ in range(6)]) #used for the id of game objects
