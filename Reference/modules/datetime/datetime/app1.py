# datetime.datetime(year, month, day, hour, minute, second,
# microsecond, tz):
# datetime -> class names
# year -> int
# month -> int
# day -> int
# hour = 0 -> int
# minute = 0 -> int
# second = 0 -> int
# microsecond = 0 -> int
# tz = None -> tzinfo
# return type -> datetime.datetime

import datetime

print(datetime.datetime(2000, 4, 13))

print(datetime.datetime(2000, 4, 13, 11,
                        25, 0, 245))
