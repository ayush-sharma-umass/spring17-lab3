import Pyro4
import time, threading
import constants.Constants as constants

from webServer.FrontEnd import FrontEnd
from webServer.BackEnd import BackEnd


@Pyro4.expose
class WebServer:

    def __init__(self, daemon, nameServer, processName):


        # Private mamebers
        self._name = processName
        self._backEnd = BackEnd()
        self._frontEnd = FrontEnd(self._backEnd, processName)

        self._registerOnServer(daemon, nameServer)


    def registerOnWebServer(self, processname):
        return self._frontEnd.registerProcesses(processname)


    def checkHeartBeat(self):
        print time.ctime() , " ", "CHECKING HEARTBEAT"
        # call the other function
        threading.Timer(10, self.checkHeartBeat).start()


    def syncWithOthers(self):

        pass

    def writeOnFile(self):
        self._backEnd.writeOnFile()

    def readFromFile(self):
        self._backEnd.readFromFile()


    def pushState(self, processname, state, logtime):
        self._frontEnd.pushState(processname, state, logtime)


    def _registerOnServer(self, daemon, nameserver):
        """
        Registering on Pyro Server.
        :param daemon: the daemon process.
        :param nameserver: the nameServer.
        :return: None
        """
        uri = daemon.register(self)
        nameserver.register(self._name, uri)
        print("Gateway registered. Name {} and uri {} ".format(self._name, uri))
