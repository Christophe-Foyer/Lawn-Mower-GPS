##This is the config file to the Lawnmower GPS project

#RTK Server, used for precise GPS positioning
RTK-Server = dict(
    # hostname or ip
    hostname = "khione.duckdns.org"
    # socket port
    port = "8384"
)

#Insert the location of your robot (for weather data, uses yahoo weather)
location = dict(
    city = 'Caen',
    country = 'France',
)

#weather conditions (don't have to edit)
weather = dict(
    # these are partial strings of weather paternas to avoid,
    # make sure to make them specific enough
    # ('freez' for instance will cover freezing rain and any string
    # with "freez" in it but will not be found in non freezing conditions)
    avoid = ["rain", "shower", "snow", "freez", "storm"] 
)

#Robot schedule
schedule = dict(
    #Daily schedule
    #Default: 9:30 to 16:00
    minHour = 9 #earliest hour it can start
    minMinutes = 30 #same with minutes
    maxHour = 16 #latest hour it can start
    maxMinutes = 0

    #Yearly Schedule
    #Default: April - October
    Months = [4, 5, 6, 7, 8, 9, 10] #Month numbers when the lawnmower is active
)

####these are random variables used as a template for now
##setting2 = 'new york'
##cabriolet = dict(
##    color = 'black',
##    engine = dict(
##        cylinders = 8,
##        placement = 'mid',
##    ),
##    doors = 2,
##)
