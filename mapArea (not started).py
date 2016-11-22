#position log based on gps.py code

#start by finding displacement vectors for each data point

movement = []

for i in range(2 len(position_log))
    moved = [position_log[i][1]-position_log[i-1][1],position_log[i][2]-position_log[i-1][2]]
    movement.append(moved)

#check angle and distance (curvature? could do, can also assume uniform magnitude?) and find first sharp turn

i=2

while angle < pi/3:
    magnitude = sqrt((movement[i-1][1])^2+(movement[i-1][2])^2)*sqrt(((movement[i][1])^2+(movement[i][1])^2))
    
    angle = acos((movement[i-1][1]*movement[i][2]+movement[i-1][2]*movement[i][2])/magnitude)
    i = i + 1

#get width of machine in meters (width)

width = 10
