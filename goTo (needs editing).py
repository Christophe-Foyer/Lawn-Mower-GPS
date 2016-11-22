def goTo(pos, tolerance): #pos if a vector [x,y]
    #goTo.py
    #goes to the location specified while staying inside the polygon defined by the map

    import savedMap #not sure how this format is gonna work out
    import insidePolygon
    import rayTracing
    import closestPoint
    import math

    if insidePolygon(pos,0):
        roboPos = getPos()
        #run until close to point
        outsidePath = savedMap['points']
        #distnce from point
        magnitude = math.sqrt((pos[0]-roboPos[0])^2+(pos[1]-roboPos[1])^2)
        while magnitude > tolerance:
            roboPos = getPos()
            magnitude = math.sqrt((pos[0]-roboPos[0])^2+(pos[1]-roboPos[1])^2)
            if rayTracing([roboPos, pos]) == 0: #raytrace between two points
                move((pos[0]-roboPos[0]),(pos[1]-roboPos[1]))
            else:
                if insidePolygon(roboPos,0):
                    move((pos[0]-roboPos[0])/magnitude*0.01,(pos[1]-roboPos[1])/magnitude*0.01)
                else:
                    closest = closestPoint(roboPos)
                    move(closest[0],closest[1])
                    #remove point from importedmap
                    ousidePath = outsidePath.remove(closest)

        return True
    else:
        print "that point is outside the boundary"
        return False
