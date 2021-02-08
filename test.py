import time
from datetime import datetime
date_num = 1557824412
loc_time = time.localtime(date_num)
print(loc_time)
timestr = time.strftime("%Y-%m-%d %H:%M:%S",loc_time)
date_test = datetime.fromtimestamp(date_num)
print(date_test)
print(timestr)