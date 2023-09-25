# import datetime
#
# date_time = datetime.datetime(2021,
#                               9,
#                               21,
#                               hour=17,
#                               minute=12,
#                               second=38,
#                               microsecond=143)
# print(f"object datetime - {date_time}")
# print(f"type {type(date_time)}")
# print(f"object datetime - {date_time.date()}")
# print(f"object datetime - {date_time.time()}\n")
#
# date_1 = datetime.date(2021, 9, 7)
# time_1 = datetime.time(5, 8, 48)
# date_time_1 = datetime.datetime.combine(date_1, time_1)
# print(f"date = {date_1}")
# print(f"time = {time_1}")
# print(f"new date - {date_time_1.replace(1980)}")
# print(f"date_time_1 = {date_time_1}\n")
#
# date_now = datetime.datetime.now()
# date_today = datetime.datetime.today()
# date_date = datetime.date.today()
# time_now = date_now.time()
# print(f"date now = {date_now}")
# print(f"date today = {date_today}")
# print(f"date date = {date_date}")
# print(f"time now = {time_now}\n")
#
# print(f"week day =  {date_now.weekday()}")
# print(f"week day method isoweekday =  {date_now.isoweekday()}\n")
#
# data_str = "28/12/2012 17:23"
# print(f"datetime to str = {date_now.strftime('%d.%m.%Y %H:%M')}")
# print(f"str to datetime = {date_now.strptime(data_str, '%d/%m/%Y %H:%M')}")
#

import os, datetime


def collector(path, res_path):
    res_path = os.path.normpath(res_path)
    path = os.path.normpath(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_time = os.path.getmtime(f"{dirpath}\\{file}")
            datetime_file = datetime.datetime.fromtimestamp(file_time)
            file_date = datetime_file.strftime("%d.%m.%Y")
            if os.path.isdir(f"{res_path}\\{file_date}"):
                os.replace(f"{dirpath}\\{file}", f"{res_path}\\{file_date}\\{file}")
            else:
                os.mkdir(f"{res_path}\\{file_date}\\")
                os.replace(f"{dirpath}\\{file}", f"{res_path}\\{file_date}\\{file}")


path = ""
res_path = ""
collector(path, res_path)