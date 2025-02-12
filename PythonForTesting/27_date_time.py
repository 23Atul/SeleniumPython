
import datetime

curDate = datetime.datetime.today().date()
# from datetime module. from datetime class. using today method. access the date
print(curDate)  # 2025-02-12


curTime = datetime.datetime.today().time()
print(curTime)  # 15:56:31.487124


curDateTime = datetime.datetime.today()
print(curDateTime)  # 2025-02-12 15:58:21.753274

# -----------------------------------------------------------------------------------------------


# Changing the Date and Time format

# strftime() ---> string format time
filename = curDateTime.strftime("%Y-%m-%d-%H-%M-%S-%f")
print(filename)  # 2025-02-12-16-02-46-622933


# url --> https://docs.python.org/3/library/datetime.html#datetime.date.isoformat
