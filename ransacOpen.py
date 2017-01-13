### maximize space within a hallway ###
# selecting two points for line
# find line
# find average distance to line
# how many are within epsilon
# repeat until k iterations, pick model with max number of inliers

#used for the square root function in distanceOfPointFromLine
import math
'''
selecting two points
- depends on location in hallway (in the middle vs to the side)
- depends on pose (facing straight down hallway vs towards the wall)
'''

'''
finding a line
- can be the mid point/line of hallway
- can extend from robot
'''

def findLineBetweenTwoPoints (x1, y1, x2, y2):
    """ Return a tuple of slope and intercept of the line going from (x1,y1) to (x2, y2) """
    lineInformationTuple = []
    #check if the line is a vertical line    
    if x1 == x2:
        lineInformationTuple.append(True)
        lineInformationTuple.append(x1)
        #Don't really need a third append here since a vertical line is x = x1
        lineInformationTuple.append(0)
    else: 
        lineInformationTuple.append(False)
        slope = (float (y2 - y1))/(float (x2 - x1))
        intercept = y1 - (slope * x1)
        lineInformationTuple.append(slope)
        lineInformationTuple.append(intercept)
    return lineInformationTuple

    
equationOfLine = findLineBetweenTwoPoints (2,5,8,5)
print("Is vertical= " + str(equationOfLine[0]))
if equationOfLine[0] == True:
    print("x = " + str(equationOfLine[1]))
else:
    print("slope = " + str(equationOfLine[1]))
    print("y intercept = " + str(equationOfLine[2]))


def distanceOfPointFromLine(x1, y1, lineInformationList):
    """ Returns the distance from point (x1, y1) to the line created from the findLineBetweenTwoPoints """
    #check if line is a vertical Line
    if  lineInformationList[0] == True:
        #vertical line is |x1 - the-distance-of-x|
        return abs(x1 - lineInformationList[1])
    elif lineInformationList[1] == 0:
        #horizontal line is just |y1 - slopeIntercept|
        return abs(y1 - lineInformationList[2])
    else:
        #distance of point between line = |ax1 + by1 + c|/ sqrt(a^2 + b^2)
        return abs((y1 - (lineInformationList[1] * x1) - lineInformationList[2])/ math.sqrt(1 + lineInformationList[1] * lineInformationList[1]))

print(str(distanceOfPointFromLine(12,8,equationOfLine)))


def avgDistOfPointsFromLine(listOfCoordinates, lineInformationList):
    """Returns the average distance of all the points from the line"""
    sumOfDistances = 0
    for coordinatePair in listOfCoordinates:
        sumOfDistances += distanceOfPointFromLine(coordinatePair[0],coordinatePair[1],lineInformationList)
    return float(sumOfDistances) / len(listOfCoordinates)
        


        

'''
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
