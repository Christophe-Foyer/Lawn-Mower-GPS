#!/usr/bin/python

#Lawnmower GPS project

#Christophe Foyer 2016

version = '2.1.1'

######ABOUT######

#This code is meant to run on raspberry pi to interface with a physical
#lawnmower, automating the lawn mowing process and is the first step before
#automating larger vehiclesU

###INSTRUCTIONS###

#Place the robot in the charging dock before running

####CHANGELOG####

#new project

###DEPENDENCIES###

##Install these packages before running this code:
dependencies = ['numpy', 'yweather', 'RPi.GPIO', 'scipy']

#####OPTIONAL#####

##optional packages (but good for performance and functions):

#none

######IMPORT######

import sys
import main

def checkDependencies():
    global dependencies
    for i in range(0, len(dependencies)):
        if not dependencies[i] in sys.modules
            return dependencies[i]
    return True

depends = checkDependencies()

########RUN########

if depends == True:
    main()
else:
    print depends + " not installed, please install before running"
