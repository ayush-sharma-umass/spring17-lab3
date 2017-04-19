import Pyro4

from constants.Constants import Constants
import random
from time import time
import timeit


@Pyro4.expose
class FrontEnd:

    def __init__(self, backend, webservername):
        self.registeredProcess = []
        self.registerProcesses.append(webservername)
        self.processToFileMap = {} # process name and its correspondong filename


        #Private members
        self._backend = backend
        self._numProcesses = 0

    def makeNewCache(self, processname):
        # make a cache for this process
        pass


    def registerProcesses(self, processname):
        self.numProcesses += 1
        self.registerProcesses.append(processname)

        filepath = Constants.FileConstants.FILE_DIR + processname + ".txt"
        self.processToFileMap[processname] = filepath
        self.makeNewCache(processname)
        return self.numProcesses



    def checkHeartBeat(self):
        # returns True if ALIVE
        pass



    def pushState(self, processname, state, logtime):
        str = logtime + ", " + processname + ", " + state
        filepath = self.processToFileMap[processname]
        self._backend.writeToFile(str, filepath)

        # write to cache

    def getState(self, processname):
        #check cache

        #if not in cache, pull from DB
        filepath = self.processToFileMap[processname]
        self._backend.readFromFile(filepath)
        pass


