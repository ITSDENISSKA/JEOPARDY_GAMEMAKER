from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep


class Timer(QThread):
    count_changed = pyqtSignal(float)

    def __init__(self, time_interval, application_window):
        super().__init__()
        self.time_interval = time_interval
        self.application_window = application_window
        self.flag = False
        self.count = 0

    def run(self):
        while True:
            if self.flag:
                self.count += 16 / self.time_interval
                sleep(0.01)
                self.count_changed.emit(self.count)
                if self.count >= 1000:
                    self.application_window.next_in_game()
