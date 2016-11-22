
def checkConditions():
    import config 
    import datetime #t = datetime.datetime.now()

    #Using numpy to save data
    import numpy

    #using yahoo weather
    import yweather

    locationID = client.fetch_woeid(config.location['city'] + ", " + config.location['country'])
    weather = client.fetch_weather(locationID, metric=True)
    t = datetime.datetime.now()
    if not t.month in config.schedule['Months']
        return False #no mowing this month
    if any(x in weather["condition"]["text"] for x in config.weather['avoid']):
        return False #no mowing in this weather
    if t.hour <= config.schedule['maxHour'] and t.hour > config.schedule['minHour']
        if t.hour = config.schedule['maxHour']
            if not t.minute <= config.schedule['maxMinutes']
                return False #no mowing right now
        elif t.hour = config.schedule['minHour']
            if not t.minute > config.schedule['minMinutes']
                return False #no mowing right now
            
    #NEED TO CHECK LAST MOW (SO IT DOESN'T MOW 15 TIMES A DAY)!
        
    numpy.save('lastMow', t, allow_pickle=True, fix_imports=True) #not sure if it works this way
    #might use databases instead of numpy
    
    return True #OH YEAH, MOWING THE LAWN
    
