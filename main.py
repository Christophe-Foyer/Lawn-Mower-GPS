######IMPORT######

#check if should run
from shouldRun import checkConditions 

#mowing routine
import mow

#charger finding routine
import findCharger

#mapping the area
import mapArea
import savedMap #not sure how this would save it yet, database would be nice

#######INIT#######

if not savedMap:
    print 'please specify areas'
    mapArea() #this should include all mowable areas and "bridges" to reach them)

#######MAIN#######

while True:
    if checkConditions() == True: ##make sure to finish this script
        #mow until battery is too low
        mowingDone = False
        cycle = 0
        #Save Charger GPS location (check charging)
        while mowingDone == False:
            cycle = cycle + 1 #count number of resumes
            mowingDone = mow(cycle) #mow until battery is low
            findCharger() #charger finding code
        #robot should finish routine in charger and wait until next mowing
    sleep(30) #wait 30 seconds between checks
    
