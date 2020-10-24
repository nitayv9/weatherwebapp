from datetime import datetime

days_hebrew = {
    'Sunday': 'יום ראשון',
    'Monday': 'יום שני',
    'Tuesday': 'יום שלישי',
    'Wednesday': 'יום רביעי',
    'Thursday': 'יום חמישי',
    'Friday': 'יום שישי',
    'Saturday': 'יום שבת'}


def get_day(string_date):
    year, month, day = (int(obj) for obj in string_date.split('-'))
    english_day = datetime(year, month, day).strftime('%A')
    return days_hebrew[english_day]