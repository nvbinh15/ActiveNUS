from datetime import datetime, timedelta

def date_end(cur_date, offset):
    """Returns the ending date of a task"""
    return cur_date + timedelta(days=offset)

def automatic_schedule(new_prog):
    pass
