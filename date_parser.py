"""docstring project"""
from dateutil import parser

day = {"1st", "2nd", "3th", "4th", "5th", "6th", "7th", "8th", "9th"}
month = {"Jan", "Feb", "Mar", "Apr", "May"}
dates = ["20th Oct 2052", "6th Jun 1933", "26th May 1960"]

def reformat_date(dates):
	"""should return YYYY-MM-DD"""
	for date in dates:
		dt = parser.parse(date)
		res = "{}-{}-{}".format(dt.year, dt.month, dt.day)
		print "{} -> {}".format(date, res)


reformat_date(dates)
