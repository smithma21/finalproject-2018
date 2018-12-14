# readme.py
# Jacob Stricker
# Mackenzie Smith

# Documentation for CS 328 Final Project

# Username cannot be generated
# Game IDs are random


# Tables 


# Players Table

# Table of players in database
# Contains player's username, password, first name, last name, age, and primary position
# Username is primary key, no values nullable except primary position

# Games Table

# Table of games in database
# Contains game ID, player's username, player's score, opponent's score, at bats, hits, runs,
# runs batted in, walks, strike outs, stolen bases, and errors
# Game ID and player username are primary keys
# No values nullable, all values default to zero except Game ID and player username


# Database Methods


# def getPlayers(self):
# Returns all players

# def getPlayer(self, username):
# Returns player information of given username

# def addPlayer(self, username, password, first_name, last_name, age, primary_position = None):
# Adds a player to the database

# def deletePlayer(self, player):
# Deletes a player from the database

# def getGame(self, id, player): 
# Returns game with given Game ID and player
# Returns none if no such game exists

# def addGame(self, id, player_username, player_score, other_score, at_bat, hits, runs, runs_batted_in, walks, strike_outs, stolen_bases, errors):
# Adds game to database 
# Game ID and player username not nullable, all other values default to zero
# Returns game information

# def deleteGame(self, game):
# Deletes game from database


# Routes

# @app.route('/', methods = ['GET'])
# def all_players():

# Returns a dictionary of links to all players in the database, along with their
# username, first name, and last name in a JSON response, 200

# @app.route('/<username>', methods = ['GET'])
# def get_player_games(username): 

# Returns a JSON response, 200 with a list of links to games that a player has participated in
# along with the player's username, a link to the player, the player's first name, last name, the game ID,
# the player's score in each game, and the opponent's score in each game
# If player not in database 404 error thrown

# @app.route('/<username>', methods = ['PUT'])
# def new_player(username):

# Adds a new player to the database
# Username must not already be taken, password, first name, last name, age, 
# and primary position arguments must be given 
# If not all arguments given 403 error is thrown 
# Returns JSON response 'ok' : 'player created', 201 if player successfully created

# @app.route('/<username>', methods = ['DELETE'])
# def delete_player(username):

# Removes a player from the database
# Username must correspond with a player, password must be provided
# If player not in database 403 error thrown
# If password not provided or incorrect, 403 error thrown

# @app.route('/<username>/<gameID>', methods = ['GET'])
# def get_game(username, gameID):

# Returns a JSON response, 200 with the game ID, the link to the game, 
# the player's score, and the opponent's score
# If no game with give game ID exists, 403 error thrown
# If no player in database with given username, 403 error thrown

# @app.route('/<username>', methods = ['POST'])
# def create_game(username):

# Adds a new game to the database
# Generates a game ID, password must be provided
# Player score, opponent score, at bats, hits, runs, runs batted in, walks, 
# strike outs, stolen bases, and errors arguments may be given but are not
# required
# If password not provided or incorrect, 403 error is thrown
# If no player in database with given username, 403 error thrown
# If game successfully added to database, JSON response with 'ok' : 'game created', 201 returned

# @app.route('/<username>/<gameID>', methods = ['DELETE'])
# def delete_game(username, gameID):

# Deletes a game from the database
# Password must be given
# If password not given or incorrect, 403 error thrown
# If game ID does not exist, 403 error thrown
# If no player in database with given username, 403 error thrown