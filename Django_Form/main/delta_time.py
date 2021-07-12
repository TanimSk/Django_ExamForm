import pytz
from datetime import datetime


class Delta_time:
    def __init__(self, timeh, timem):
        bst = pytz.timezone('Asia/Dhaka')

        self.h = int(timeh) - int(datetime.now(bst).strftime("%H"))
        self.m = int(timem) - int(datetime.now(bst).strftime("%M"))
        self.s = 60 - int(datetime.now(bst).second)

        if self.m < 0:
            self.m = 60 + self.m
            self.h -= 1
