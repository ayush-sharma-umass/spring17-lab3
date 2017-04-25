from lockfile import LockFile, LockTimeout
import os

class DatabaseManager:

    def __init__(self):
        pass


    def createFile(self, filepath):
        if not os.path.isfile(filepath):
            file = open(filepath, "w")
            file.close()
            return True
        return False


    def readFile(self, filepath, numRows):
        lock = LockFile(file)
        while not lock.i_am_locking():
            try:
                lock.acquire(timeout=60)  # wait up to 60 seconds
            except LockTimeout:
                lock.break_lock()
                lock.acquire()
        if not os.path.isfile(filepath):
            file = open(filepath, "w")
        else:
            file = open(filepath, "a")
        output = []
        counter = 1
        for line in reversed(open(filepath).readlines()):
            stringData = line.rstrip().split(",")
            if counter <= numRows:
                output.append(stringData)
                counter += 1
            else:
                break
        file.close()
        lock.release()
        return output


    def writeFile(self, data, filepath):
        lock = LockFile(filepath)
        while not lock.i_am_locking():
            try:
                lock.acquire(timeout=60)  # wait up to 60 seconds
            except LockTimeout:
                lock.break_lock()
                lock.acquire()
        if not os.path.isfile(filepath):
            file = open(filepath, "w")
        else:
            file = open(filepath, "a")
        file.write(data)
        file.close()
        lock.release()






