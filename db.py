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
   #games = relationship('Game', back_populates = 'players')

   def __init__(self, username, password, first_name, last_name, age, primary_position):
       self.username = username
       self.password = password
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.primary_position = primary_position

   def __repr__(self):
       #return object type in blue and all variable names in yellow the values held by the variables will be printed in the default white.
       return (blue("Player\n")\
           + yellow("username") + white(": %s\n")\
           + yellow("first_name") + white(": %s\n")\
           + yellow("last_name") + white(": %s\n")\
           + yellow("age") + white(": %d\n")\
           + yellow("primary_position") + white(": %s\n"))\
           %(self.username, self.first_name, self.last_name, self.age, self.primary_position)

#Game table here

class Game(Base):
   __tablename__ = 'games'

   id = Column(String, nullable = False, primary_key = True) #The game id is random and will not take a value from the user, if a user provides a game name or id it will be discarded
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

   def __init__(self, id, player_score, other_score, at_bat, hits, runs, runs_batted_in, walks, strike_outs, stolen_bases, errors): #add more args
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
       return (blue_text + "Game\n"\
           + yellow("id") + white(": %s\n")\
           + yellow("player_score") + white(": %d\n")\
           + yellow("other_score") + white(": %d\n")\
           + yellow("at_bat") + white(": %d\n")\
           + yellow("hits") + white(": %d\n")\
           + yellow("runs") + white(": %d\n")\
           + yellow("runs_batted_in") + white(": %d\n")\
           + yellow("walks") + white(": %d\n")\
           + yellow("strike_outs") + white(": %d\n")\
           + yellow("stolen_bases") + white(": %d\n")\
           + yellow("errors") + white(": %d\n"))\
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

def getGame(self): #add args
    pass

def addGame(self): #add args
    pass

def deleteGame(self):   #possibility this function wont be used
    pass

#Helper Functions

def white(text):
    white_text = "\033[0m "
    new = white_text + text
    return new

def blue(text):
    blue_text = "\033[1;34;40m "
    new = blue_text + text
    return new

def red(text):
    red_text = "\033[0;31;47m "
    new = red_text + text
    return new

def yellow(text):
    yellow_text = "\033[0;33;47m "
    new = yellow_text + text
    return new

player = Player(username = "smithma21", password = "password", first_name = "Mackenzie", last_name = "Smith", age = 20, primary_position = "Center Field")
print (repr(player))
