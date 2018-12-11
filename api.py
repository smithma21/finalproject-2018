#NAMES
#Jacob Stricker
# Mackenzie Smith


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
    checkusername(username)

    password = request.args.get('password')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    age = request.args.get('age')
    primary_position = request.args.get('primary_position')

    if password or first_name or last_name \
    or age or primary_position == None:
    	abort(403, 'must provide all arguments')


    player = db.addPlayer(username, password, first_name, last_name, age, primary_position)
    
    db.commit()

    return make_json_response({ 'ok' : 'player created' }, 201)

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
    gameID = makeId()
    player_username = None
    
    password = request.args.get('password')
    if password == None:
        abort(403, 'must provide a password')
    players = db.getPlayers()
	for player in players:
		if player.username == username and player.password == password:
			player_username = player.username
			looper = True
			while (looper):
            	for game in player.games:
                	gameID = makeId()
                	if game.id == gameID:
                		looper = True
                looper = False
            player_score = request.args.get('player_score')
    		other_score = request.args.get('other_score')
    		at_bats = request.args.get('at_bats')
    		hits = request.args.get('hits')
    		runs = request.args.get('runs')
    		runs_batted_in = request.args.get('runs_batted_in')
    		walks = request.args.get('walks')
    		strike_outs = request.args.get('strike_outs')
    		stolen_bases = request.args.get('stolen_bases')
    		errors = request.args.get('errors')

    		game = db.addGame(gameID, player_username, player_score, other_score, at_bats, hits, runs, runs_batted_in, walks, strike_outs, stolen_bases, errors)

    		db.commit()


    		return make_json_response({ 'ok' : 'game created' }, 201)

        elif player.username == username and player.passowrd != password:
        	abort (403, "Wrong password")
	abort (404, "Player does not exist")

@app.route('/<username>/<gameID>', methods = ['DELETE'])
def delete_game(username, gameID):
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

def checkusername(username):
	player = db.getPlayer(username)
   
	if player is not None:
    	abort(403, 'username already exists')
