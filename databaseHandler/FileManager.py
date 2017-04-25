import time

class FileManager:




    def __init__(self, fileName):
        self.fileName = fileName

        pass


    def acquireLock(self):
        self.lock = True

    def releaseLock(self):
        self.lock = False

    def writeFile(self):
        if self.lock == False:
            self.acquireLock()
            print "Writing now"
            time.sleep(5)
            # go ahead with writing
            pass
            self.releaseLock()
        else:
            while self.lock == False:
                # wait for release of lock
                pass
            # acquire lock
            self.acquireLock()
            # do the changes
            print "writing now"
            time.sleep(5)

            #release lock
            self.releaseLock()

    def readFile(self):
        if self.lock == False:
            self.acquireLock()
            # go ahead with reading
            self.releaseLock()
            pass
        else:
            while self.lock == False:
                # wait for release of lock
                pass
            # acquire lock
            self.acquireLock()
            # read from the file
            #release lock
            self.releaseLock()


