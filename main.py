# 运行逻辑

from process import MainThread
from config import *

class Velocity(MainThread):
    def __init__(self):
        MainThread.__init__(
            self,
            args='sh run.sh',
        )


if __name__ == '__main__':
    Velocity()
