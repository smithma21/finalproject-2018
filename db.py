# Sets up database
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from json import dumps

#Colored Text
red_text = "\033[0;31;47m "
green_text = "\033[0;32;47m "
yellow_text = "\033[0;33;47m "
blue_text = "\033[1;34;40m "
grey_text = "\033[0;30;47m "

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
       return (blue_text + "Player\n"\
           + yellow_text + "username" + ": " + "%s\n"\
           + yellow_text + "first_name" + ": " + "%s\n"\
           + yellow_text + "last_name" + ": " + "%s\n"\
           + yellow_text + "age" + ": " + '%d' + "\n"\
           + yellow_text + "primary_position" + ": " + "%s\n")\
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

   def __init__(self, id, player_score, other_score, at_bat, hits, runs, runs_batted_in, walks, strike_outs, errors): #add more args
       self.id = self.id
       self.player_score = player_score
       self.other_score = other_score
       self.at_bat = at_bat
       self.hits = hits
       self.runs = runs
       self.runs_batted_in = runs_batted_in
       self.walks = walks
       self.strike_outs = strike_outs
       self.errors = errors

   def __repr__(self):
       return blue_text + "Game\n"\
           + yellow_text + "id" + ": " + "%s\n"\
           + yellow_text + "player_score" + ": " + "%d\n"\
           + yellow_text + "other_score" + ": " + "%d\n"\
           + yellow_text + "at_bat" + ": " + "%d\n"\
           + yellow_text + "hits" + ": " + "%d\n"\
           + yellow_text + "runs" + ": " + "%d\n"\
           + yellow_text + "runs_batted_in" + ": " + "%d\n"\
           + yellow_text + "walks" + ": " + "%d\n"\
           + yellow_text + "strike_outs" + ": " + "%d\n"\
           + yellow_text + "stolen_bases" + ": " + "%d\n"\
           + yellow_text + "errors" + ": " + "%d\n"\
           %(self.id, self.player_score, self.other_score, self.at_bat, self.hits, self.runs_batted_in, self.walks, self.strike_outs, self.errors)

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
    return buckets

def getPlayer(self, username):
    pass

def addPlayer(self, username, password, first_name, last_name, age, prefered_position = None):
    pass

def deletePlayer(self, player):
    pass

def getGame(slef): #add args
    pass

def addGame(self): #add args
    pass

def deleteGame(self):   #possibility this function wont be used
    pass

player = Player(username = "smithma21", password = "password", first_name = "Mackenzie", last_name = "Smith", age = 20, primary_position = "Center Field")
print (player.username)
print(player.password)
print(player.first_name)
print(player.last_name)
print(player.age)
print(player.primary_position)
print (repr(player))