import Pyro4
import time
from constants.Constants import Constants

@Pyro4.expose
class Sensor:

    def __init__(self, daemon, nameServer, webServer, processName):
        self.state = Constants.SensorConstants.STATE_OFF
        self.processName = processName

        #private members
        self._pid = -1
        self._webServer = webServer
        self._registerOnserver(daemon, nameServer)



    def registerOnWebServer(self):
        proxyName = "PYRONAME:" + self._webServer
        webServerProxy = Pyro4.Proxy(proxyName)
        print("Registering {} with gateWay: {} and gatewayProxy: {}".format(self._name, self._gatewayName, webServerProxy))
        self._pid = webServerProxy.register(self._name)


    def pushState(self):
        proxyName = "PYRONAME:" + self._webServer
        webServerProxy = Pyro4.Proxy(proxyName)
        curtime = time.time()
        webServerProxy.pushState(self.state, self._name, curtime)


    def pullState(self):
        curtime = time.time()
        return curtime, self.state

    def chageState(self):
        if self.state == Constants.SensorConstants.STATE_OFF:
            self.state = Constants.SensorConstants.STATE_ON
        else:
            self.state = Constants.SensorConstants.STATE_OFF

    def _registerOnserver(self, daemon, nameserver):
        """
        Registering on Pyro Server.
        :param daemon: the daemon process.
        :param nameserver: the nameServer.
        :return: None
        """
        uri = daemon.register(self)
        nameserver.register(self._name, uri)
        print("Sensor registered. Name {} and uri {} ".format(self._name, uri))

