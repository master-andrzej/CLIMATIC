import threading
import time
_HUMIDITY = 0
_TEMPERATURE = 0

from GUI import view, model
from threading import Thread

class Controller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.viewTemp = view.View

    def run(self):
        self.view = self.viewTemp()
        self.view.run()


if __name__ == '__main__':
    testApp = Controller()
    testApp.start()
