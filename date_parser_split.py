"""docstring project"""
from dateutil import parser

day = {"1st": '01', "2nd": '02', "3th": '03', "4th": '04', "5th": '05', "6th": '06', "7th": '07', "8th": '08', "9th": '09'}
month = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05'}
dates = ["2nd Feb 2052", "6th Mar 1933", "9th May 1960"]

def reformat_date(dates):
	"""should return YYYY-MM-DD"""
	for date in dates:
		date_split = date.split(' ')
		YYYY = date_split[2]
		MM = month[date_split[1]]
		DD = day[date_split[0]]
		res = '{}-{}-{}'.format(YYYY, MM, DD)
		print res


reformat_date(dates)
