# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days

import re
import datetime

def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    def get_date(date_):
        return datetime.datetime.strptime(date_, '%d %b %Y')
    
    def get_Age(race_dob):
        race, dob = race_dob
        race, dob = get_date(race), get_date(dob)
        return divmod((race - dob).days, 365.25)
    
    def get_racetime(line):
        return re.findall(r'\d{2}:\S+', line)[0]
    
    time = get_racetime(line)
    event_dob = re.findall(r'\d{2} \w{3} \d{4}', line)
    age = get_Age(event_dob)
    return (age, time)
    
def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()
    race_Age = []
    for line in races.splitlines():
        if 'Jennifer Rhines' in line:
            race_Age.append(get_event_time(line))
    slowest_race = max(race_Age, key=lambda x: x[1])
    slowest_age, slowest_racetime = slowest_race

    def format_date(age):
        years, days = age
        return f'{int(years)}y{int(days)}d'
    
    return (format_date(slowest_age), slowest_racetime)