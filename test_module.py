import pytest
from main import *

def test_split_time():
    time = "3:10"
    expected_result = ["3", "10"]
    assert split_time(time) == expected_result

def test_add_hours():
    h1 = "3"
    h2 = "7"
    assert add_hours(h1, h2) == 10

def test_format_hour():
    hour = 14
    assert format_hour(hour) == (2, 1)

def test_format_minute():
    minute = 64
    assert format_minute(minute) == (4, 1)

def test_add_time():
    assert add_time("3:00 PM", "3:10") == "6:10 PM"
    assert add_time("11:30 AM", "2:32", "Monday") == "2:02 PM, Monday"
    assert add_time("11:43 AM", "00:20") == "12:03 PM"
    assert add_time("10:10 PM", "3:30") == "1:40 AM (next day)"
    assert add_time("11:43 PM", "24:20", "tueSday") ==  "12:03 AM, Thursday (2 days later)"
    assert add_time("6:30 PM", "205:12") == "7:42 AM (9 days later)"