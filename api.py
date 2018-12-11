#NAMES
#Jacob Stricker


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
def get_players_games(username):
    players = db.getPlayers()
    games = []
    for player in players:
        if username == player.username:
            for game in player.games:
                games.append({'id':game.id, 'link': "/"+game.id, 'player score' : game.player_score, 'oppenent score' : game.other_score})
            player = {'username' : player.username, 'link' : '/'+player.username, 'first name' : player.first_name, 'last name' : player.last_name, 'games' : games}
            return make_json_response(player, 200)
    abort(404,'Person does not exist')

@app.route('/<username>', methods = ['PUT'])
def new_player(username):
    pass

@app.route('/<username>', methods = ['DELETE'])
def delete_player(username):
    password = request.args.get('password')
    if password == None:
       abort(403, 'must provide a password')
    players = db.getPlayers()
    for player in players:
        if player.username == username and player.password == password:
            db.deletePlayer(player)
            db.commit()
        elif player.username == username and player.passowrd != password:
            abort (403, "Wrong password")
    abort (404, "No Player")

@app.route('/<username>/<gameID>', methods = ['GET'])
def get_game(username, gameID):
    players = db.getPlayers()
    for player in players:
        if username == player.username:
            for game in player.games:
                if game.id == gameID:
                    wanted_game = {'id':game.id, 'link': "/"+game.id, 'player score' : game.player_score, 'oppenent score' : game.other_score}
                    return make_json_response(wanted_game, 200)
            abort(403, "Game does not exist")
    abort(404,'Person does not exist')

@app.route('/<username>', methods = ['POST'])
def create_game(username):
    pass

@app.route('/<username>/<gameID>', methods = ['DELETE'])
def delete_game(username, gameID):
    def delete_player(username):
        password = request.args.get('password')
        if password == None:
           abort(403, 'must provide a password')
        players = db.getPlayers()
        for player in players:
            if player.username == username and player.password == password:
                for game in player.games:
                    if game.id == gameID:
                        db.deleteGame(game)
                        db.commit()
                abort(403, "Game does not exist")
            elif player.username == username and player.passowrd != password:
                abort (403, "Wrong password")
        abort (404, "Player does not exist")

# Starts the application
if __name__ == "__main__":
   app.run()

#Helper Function(s)
def makeId():
   return ''.join([random.choice(alphabet) for _ in range(6)]) #used for the i
