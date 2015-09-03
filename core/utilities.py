from enum import Enum

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def addVector(a, b):
    (x0, y0, z0) = a
    (x1, y1, z1) = b
    return (x0+x1, y0+y1, z0+z1)

def getRelVector(a, b):
    (x0, y0, z0) = a
    (x1, y1, z1) = b
    return (x1-x0, y1-y0, z1-z0)

class InvalidMoveException(Exception):
    def __init__(self, message=""):
        self.message = "Invalid Move!" + message

class Color(Enum):
    black = "black"
    white = "white"