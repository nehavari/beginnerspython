from unittest.mock import Mock
from datetime import datetime

# day is date
tuesday = datetime(year=2023, month=1, day=2)
saturday = datetime(year=2023, month=1, day=21)

datetime = Mock()

def is_weekday():
	today = datetime.today()
	return 0 <= today.weekday() < 5
print("checking weekend")
datetime.today.weekday.return_value = saturday
assert not is_weekday()
print("checking weekday")
datetime.today.weekday.return_value = tuesday
assert is_weekday()
