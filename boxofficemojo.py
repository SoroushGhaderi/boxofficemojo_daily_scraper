import requests
import pandas as pd
import datetime
import time
import os

os.mkdir("datasets")

# From start_date to end_date create dates and add 1 day for creating list of dates
def create_range_of_time(start_date, end_date, days= 1):
    date = start_date
    list_of_dates = []
    while date != end_date:
        list_of_dates.append(date)
        detla = datetime.timedelta(days)
        date += detla
    return list_of_dates

# Start Date
year_start = int(input("Please input your year of start date: "))
month_start = int(input("Please input your month of start date: "))
day_start = int(input("Please input your day of start date: "))

# End Date
year_end = int(input("Please input your year of end date: "))
month_end = int(input("Please input your month of end date: "))
day_end = int(input("Please input your day of end date: "))

start_date = datetime.date(year_start, month_start, day_start)
end_date = datetime.date(year_end, month_end, day_end)
list_of_dates_normal_format = create_range_of_time(start_date, end_date)
list_of_dates_boxofficemojo_format = [loop_date.strftime("%Y-%m-%d") for loop_date in list_of_dates_normal_format]

list_dict = {}
for item in list_of_dates_boxofficemojo_format:
    list_dict[item] = []

for date,item in zip(list_of_dates_boxofficemojo_format, list_dict):
    url= "https://www.boxofficemojo.com/date/{}/?ref_=bo_da_nav".format(date)
    date = pd.read_html(url)
    time.sleep(10)
    list_dict[item].append(date[0])
    list_dict[item][0].to_csv("datasets/{}.csv".format(item), index= False)
    print("boxoffice domestic gross {} is saved".format(item))
    