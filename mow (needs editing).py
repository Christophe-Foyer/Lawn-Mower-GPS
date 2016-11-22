def mow(cycle):

    #gpsClient to communicate with the RTK server (accurate GPS)
    import gpsClient

    #GPS library (still have to figure out which one)
    import $gpsLibrary

    #System stuff
    import platform
    import sys
    import time
    import Queue
    import threading
    import multiprocessing
    import RPi.GPIO as GPIO
    import time
    import subprocess
    import os
    import datetime #t = datetime.datetime.now()

    ###import the map file
    import savedMap #not sure which format

    import drawPath

    drawPath(savedMap) #draws the path the robot should follow (hopefully this is the same every time and fairly fast, otherwise I should save it for later)

    if cycle > 1:
        import lastPos #not sure which format
        goTo(lastPos, 0.1) #tolerance of 10cm
        status = followPath(lastPos) #follow path starting from lastPos
    else:
        status = followPath('start') #follow from start
        #now reach that position rapidly (while trying to stay on the lawn and using bridge)
        #make sure to be careful when using "bridges"
    return status

