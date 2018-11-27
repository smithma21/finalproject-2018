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

#Routes

#Helper Function(s)
def makeId():
   return ''.join([random.choice(alphabet) for _ in range(6)]) #used for the id of game objects