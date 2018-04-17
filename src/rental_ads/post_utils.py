from uszipcode import ZipcodeSearchEngine

from .states import states

def states_choices():
    # states dropdown
    STATE_CHOICE = []

    for key, value in states.items():
        STATE_CHOICE.append((key, value))

    return STATE_CHOICE

def search_city(state):
    search_engine = ZipcodeSearchEngine()
    state = search_engine.by_city(str(state))
    
    cities = []
    for i in state:
        cities.append(i.City)

    return cities

def search_zip(city):

    search_engine = ZipcodeSearchEngine()
    city = search_engine.by_city(str(city))

    zipcodes = []
    for i in city:
        zipcodes.append(i.Zipcode)

    return zipcodes


