from datetime import datetime, timedelta, date
from supermemo2 import SMTwo, mon_day_year


def day_difference(start, end):
    return (end-start).days

def date_end(cur_date, offset):
    return cur_date + timedelta(days=offset)

def automatic_schedule(new_prog):
    pass
