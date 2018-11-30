# Sets up database
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from json import dumps

Base = declarative_base()

#Player table here

class Player(Base):
   __tablename__ = 'players'
   
   #Log in info
   username = Column(String, nullable = False, primary_key = True)
   password = Column(String, nullable = False)
   #account info
   first_name = Column(String, nullable = False)
   last_name = Column(String, nullable = False)
   age = Column(Integer, nullable = False)
   primary_position = Column(String)
   games = relationship('Game', back_populates = 'player')

   def __init__(self, username, password, first_name, last_name, age, primary_position):
       self.username = username
       self.password = password
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.primary_position = primary_position

   def __repr__(self):
       #return object type in blue and all variable names in yellow the values held by the variables will be printed in the default white.
       return (cyan("Player\n")\
           + green("username") + white(": %s\n")\
           + green("first_name") + white(": %s\n")\
           + green("last_name") + white(": %s\n")\
           + green("age") + white(": %d\n")\
           + green("primary_position") + white(": %s\n"))\
           %(self.username, self.first_name, self.last_name, self.age, self.primary_position)

#Game table here

class Game(Base):
   __tablename__ = 'games'

   id = Column(String, nullable = False, primary_key = True) #The game id is random and will not take a value from the user, if a user provides a game name or id it will be discarded
   player_username = Column(String, ForeignKey('players.username', ondelete="CASCADE"), nullable = False, primary_key = True)
   player_score = Column(Integer, nullable = False, default = 0)
   other_score = Column(Integer, nullable = False, default = 0)
   at_bats = Column(Integer, nullable = False, default = 0)
   hits = Column(Integer, nullable = False, default = 0)
   runs = Column(Integer, nullable = False, default = 0)
   runs_batted_in = Column(Integer, nullable = False, default = 0)
   walks = Column(Integer, nullable = False, default = 0)
   strike_outs = Column(Integer, nullable = False, default = 0)
   stolen_bases = Column(Integer, nullable = False, default = 0)
   errors = Column(Integer, nullable = False, default = 0)
   player = relationship("Player", back_populates = 'games')

   def __init__(self, id, player_score, other_score, at_bat, hits, runs, runs_batted_in, walks, strike_outs, stolen_bases, errors):
       self.id = self.id
       self.player_score = player_score
       self.other_score = other_score
       self.at_bat = at_bat
       self.hits = hits
       self.runs = runs
       self.runs_batted_in = runs_batted_in
       self.walks = walks
       self.strike_outs = strike_outs
       self.stolen_bases = stolen_bases
       self.errors = errors

   def __repr__(self):
       return (cyan("Game\n")\
           + green("id") + white(": %s\n")\
           + green("player_score") + white(": %d\n")\
           + green("other_score") + white(": %d\n")\
           + green("at_bat") + white(": %d\n")\
           + green("hits") + white(": %d\n")\
           + green("runs") + white(": %d\n")\
           + green("runs_batted_in") + white(": %d\n")\
           + green("walks") + white(": %d\n")\
           + green("strike_outs") + white(": %d\n")\
           + green("stolen_bases") + white(": %d\n")\
           + green("errors") + white(": %d\n"))\
           %(self.id, self.player_score, self.other_score, self.at_bat, self.hits,  selif.runs, self.runs_batted_in, self.walks, self.strike_outs, self.stolen_bases, self.errors)

#Database set up here

class Db:
   def __init__(self):
      engineName = 'sqlite:///test.db'
      self.engine = create_engine(engineName)
      self.metadata = Base.metadata
      self.metadata.bind = self.engine
      self.metadata.drop_all(bind=self.engine)
      self.metadata.create_all(bind=self.engine)
      Session = sessionmaker(bind=self.engine)
      self.session = Session()

   def commit(self):
      self.session.commit()

   def rollback(self):
      self.session.rollback()

#Database methods here

def getPlayers(self):
    players = self.session.query(Player).all()
    return players

def getPlayer(self, username):
    players = self.session.query(Player).all()
    for user in players:
        if user.username == username:
            return user

def addPlayer(self, username, password, first_name, last_name, age, primary_position = None):
    player = Player(username = username, password = password,\
       first_name = first_name, last_name = last_name, age = age, primary_position = primary_position)
    self.session.add(player)

def deletePlayer(self, player):
    self.session.delete(player)

def getGame(self, id, player): 
    games = self.session.query(Game).all()
    for game in games:
        if game.player == player:
            return game
        return None

def addGame(self, id, player_username, player_score, other_score, at_bat, hits, runs, runs_batted_in, walks, strike_outs, stolen_bases, errors):
    game = Game(id = id, player_username = player_username, player_score = player_score, other_score = other_score,\
       at_bat = at_bat, hits = hits, runs = runs, runs_batted_in = runs_batted_in, walks = walks,\
      strike_outs = strike_outs, stolen_bases = stolen_bases, errors = errors)
    self.session.add(game)
    return(game)

def deleteGame(self, game):
    self.session.delete(game)

#Helper Functions

def white(text):
    white = "\033[0m "
    new = white + text
    return new

def red(text):
    red = "\033[0;31;40m "
    new = red + text
    return new

def green(text):
    green = "\033[0;32;40m "
    new = green + text
    return new

def blue(text):
    blue = "\033[0;34;40m "
    new = blue + text
    return new

def yellow(text):
    yellow = "\033[0;33;40m "
    new = yellow + text
    return 

def cyan(text):
    cyan  = "\033[0;36;40m"
    new = cyan + text
    return new

def purple(text):
    purple  = "\033[0;35;40m"
    new = purple + text
    return new

#tests

player = Player(username = "smithma21", password = "password", first_name = "Mackenzie", last_name = "Smith", age = 20, primary_position = "Center Field")
print (repr(player))
