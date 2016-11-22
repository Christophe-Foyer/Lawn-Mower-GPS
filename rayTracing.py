#uses raytracing to count the number of intercepts between two points

def rayTracing(points, pointMap):

    #finds line intersects
    def line_intersection(line1, line2):
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
           return False

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y

    #counts line intersects in map
    point1 = points[0]
    point2 = points[1]
    intercepts = 0
    for i in range(len(pointMap)):
        if i+1 <= len(pointMap):
            j = i+1
        else:
            j = 0
        line_intersection((point1, point2), (pointMap[i], pointMap[j]))
        
        if intercept != False:
            #there's probably better ways of doing this, eh!
            if pointMap[i][0] > pointMap[j][0]
                xmin = pointMap[j][0]
                xmax = pointMap[i][0]
            else:
                xmin = pointMap[i][0]
                xmax = pointMap[j][0]
            if pointMap[i][1] > pointMap[i][1]
                ymin = pointMap[j][1]
                ymax = pointMap[i][1]
            else:
                ymin = pointMap[i][1]
                ymax = pointMap[j][1]
            if (xmin < intercept[0] <= xmax) and (ymin < intercept[1] <= ymax):
                if isinstance(points[1], list):
                    if pointMap[i][1] > pointMap[i][1]
                        xmin = pointMap[j][0]
                        xmax = pointMap[i][0]
                    else:
                        xmin = pointMap[i][0]
                        xmax = pointMap[j][0]
                    if pointMap[i][1] > pointMap[i][1]
                        ymin = pointMap[j][1]
                        ymax = pointMap[i][1]
                    else:
                        ymin = pointMap[i][1]
                        ymax = pointMap[j][1]
                    if :
                        intercepts += 1
                else:
                    intercepts += 1
    return intercepts


