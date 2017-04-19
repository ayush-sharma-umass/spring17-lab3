import Pyro4
from constants.Constants import Constants

@Pyro4.expose
class Device:

    def __init__(self, daemon, nameServer, webServer, processName):
        self.state = Constants.DeviceConstants.STATE_OFF
        self.processName = processName
        self.webServer = webServer
        self._registerOnserver(daemon, nameServer)

    def registerOnServer(self):
        proxyName = "PYRONAME:" + self._webServer
        webServerProxy = Pyro4.Proxy(proxyName)
        print("Registering {} with gateWay: {} and gatewayProxy: {}".format(self._name, self._gatewayName, webServerProxy))
        self._pid = webServerProxy.register(self._name)


    def pushState(self):
        proxyName = "PYRONAME:" + self._webServer
        webServerProxy = Pyro4.Proxy(proxyName)
        webServerProxy.pushState(self.state, self._pid)

    def pullState(self):
        curtime = time.time()
        return curtime, self.state

    def changeState(self):
        if self.state == Constants.DeviceConstants.STATE_OFF:
            self.state = Constants.DeviceConstants.STATE_ON
        else:
            self.state = Constants.DeviceConstants.STATE_OFF

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
        pass