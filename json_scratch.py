"""Request JSON data from URL and query for info.

For the stock open and close prices on each date when keekday
is weekDay if the stock information is available.
"""

import json
from datetime import datetime
import calendar
# import requests


# response = requests.get("https://jsonmock.hackerrank.com/api/stocks/?page=2")
# todos = json.loads(response.text)
# with open('data_paginated.json', 'w') as write_data:
#    json.dump(todos, write_data, indent=4)

with open('data.json', 'r') as read_data:
    json_data = json.load(read_data)


def open_and_close_prices(data, first_date, last_date, week_day):
    """Search stock info if available."""
    start_date = datetime.strptime(first_date, '%d-%B-%Y')
    end_date = datetime.strptime(last_date, '%d-%B-%Y')
    print('From {} to {}'.format(start_date, end_date))

    for stock_data in data['data']:
        stock_date = datetime.strptime(stock_data['date'], '%d-%B-%Y')
        weekday = calendar.day_name[stock_date.weekday()]
        if(stock_date >= start_date and
            stock_date <= end_date and
            week_day == weekday
        ):
            print('{} {} {}'.format(stock_data['date'], stock_data['open'], stock_data['close']))


open_and_close_prices(json_data, '5-January-2000', '22-February-2000', 'Monday')
