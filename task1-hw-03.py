from datetime import datetime, date, timedelta

today = date.today()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

def get_days_from_today(date):
    format_date = string_to_date(date)
    delta = (today - format_date).days
    return delta
   
date_calc_str = input("Enter date in format YYYY-mm-dd: ")    
print(get_days_from_today(date_calc_str))

