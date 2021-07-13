import pytz
from datetime import datetime


class Delta_time:
    def __init__(self, time_s):
        bst = pytz.timezone('Asia/Dhaka')
        time_s = int(time_s)         # dead sec
        current_time = int(datetime.now(bst).strftime("%H")) * 60 * 60 + int(datetime.now(bst).strftime("%M")) * 60 + int(datetime.now(bst).second)
        self.passed_s = (time_s - current_time)
        delta = self.passed_s / 3600
        self.h = int(delta)
        delta = (delta - self.h) * 60
        self.m = int(delta)
        self.s = int((delta - self.m) * 60)

# t = Delta_time(12*(60*60) + 28*60)
# print(t.h, t.m, t.s)
