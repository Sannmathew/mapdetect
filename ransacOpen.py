### maximize space within a hallway ###
# selecting two points for line
# find line
# find average distance to line
# how many are within epsilon
# repeat until k iterations, pick model with max number of inliers

'''
selecting two points
- depends on location in hallway (in the middle vs to the side)
- depends on pose (facing straight down hallway vs towards the wall)

finding a line
- can be the mid point/line of hallway
- can extend from robot

average distance to line
- ransac regression-ish algorithm

how many within epsilon
- found after distance calculated for points

'''

'''

simple case: robot data we were given

take 0, 180 degree points, get midpoint, make line to 90 degree point returned ffrom data

do regression, find average distance

'''
