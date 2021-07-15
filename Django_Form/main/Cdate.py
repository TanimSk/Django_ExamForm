import pytz
from datetime import datetime

def this_date():
    bst = pytz.timezone('Asia/Dhaka')
    return int(str(datetime.now(bst).strftime("%Y")) + str(datetime.now(bst).strftime("%m")) + str(datetime.now(bst).strftime("%d")))
