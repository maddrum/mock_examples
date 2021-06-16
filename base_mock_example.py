# https://realpython.com/python-mock-library/
import datetime
from unittest.mock import Mock

tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5


datetime.datetime.today.return_value = tuesday
# Test if today is a weekday
assert is_weekday()

datetime.datetime.today.return_value = saturday
# Test if today is a weekday
assert is_weekday()
