import Pyro4

import constants.Constants as constants
import random
from time import time
import timeit


@Pyro4.expose
class BackEnd:

    def __init__(self):
        # set up a database connection

        pass


    def createFile(self):
        # request file manager to make a file
        pass

    def writeToFile(self, string, filepath):
        # if file not exists create file of that name
        # write to that file
        pass

    def readFromFile(self, filename):
        # if filename exits:
        # read top entry an return
        pass
