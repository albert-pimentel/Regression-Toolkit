
from graphics import *
import ctypes
import SimpleRegression


# Visualizes a simple linear regression model as a set of points on a graph
# alongside the computed line of best fit
# Input: Two arrays of equal length (n)
# Output: None
# Runtime: O(n)
def drawSimpleRegression(xData, yData):
    if len(xData) != len(yData):
        raise RuntimeError("Must have one response data point per explanatory data point")

    # Set graph size based on screen resolution
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0) - 300
    height = user32.GetSystemMetrics(1) - 300
    win = GraphWin("Simple Regression", width, height)

    # Draw title
    titlePt = Point(width / 2, 25)
    title = Text(titlePt, "Simple Regression Visualization")
    subtitlePt = Point(width / 2, 45)
    subtitle = Text(subtitlePt, "By Albert Pimentel")
    title.draw(win)
    subtitle.draw(win)

    # Draw axes
    drawAxes(width, height, win)
    # Mark x and y axes
    labelXYAxes(width, height, win)
    # Add markers along axes
    addMarkers(width, height, win, xData, yData)
    # Draw points on graph
    drawPoints(width, height, win, xData, yData,)
    # Draw line of best fit
    drawLineOfBestFit(width, height, win, xData, yData)
    # Close window on click and after program ends
    win.getMouse()
    win.close()


# Draws the X and Y axes of the graph
# Input: Width of window, height of window, window object
# Output: None
# Runtime: O(1)
def drawAxes(width, height, window):
    topLeft = Point(50, 50)
    bottomLeft = Point(50, height - 50)
    bottomRight = Point(width - 50, height - 50)
    line1 = Line(topLeft, bottomLeft)
    line2 = Line(bottomLeft, bottomRight)
    line1.draw(window)
    line2.draw(window)


# Labels the X and Y axes of the graph
# Input: Width of window, height of window, window object
# Output: None
# Runtime: O(1)
def labelXYAxes(width, height, window):
    # Mark x and y axes
    xLabelPt = Point(40, 50)
    xLabel = Text(xLabelPt, "y")
    yLabelPt = Point(width - 50, height - 40)
    yLabel = Text(yLabelPt, "x")
    xLabel.draw(window)
    yLabel.draw(window)


# Adds 10 markers along the axes of the graph to give a better idea
# of where points lie
# Input: Width of window, height of window, window object, explanatory data, response data
# Output: None
# Runtime: O(n)
def addMarkers(width, height, window, xData, yData):
    # Add 10 markers along each axis
    xIncrement = (width - 100) / 10
    yIncrement = (height - 100) / -10
    currentXCoord = 50
    currentYCoord = height - 50
    for i in range(10):
        # Draw marker on x-axis
        xPt1 = Point(currentXCoord, height - 60)
        xPt2 = Point(currentXCoord, height - 40)
        xLine = Line(xPt1, xPt2)
        xLine.draw(window)
        # Place corresponding number below marker
        xTextPt = Point(currentXCoord, height - 30)
        xText = Text(xTextPt, str(min(xData) + (i * (max(xData) - min(xData)) / 10)))
        xText.draw(window)

        # Draw marker on y-axis
        yPt1 = Point(40, currentYCoord)
        yPt2 = Point(60, currentYCoord)
        yLine = Line(yPt1, yPt2)
        yLine.draw(window)
        # Place corresponding number left of marker
        yTextPt = Point(25, currentYCoord)
        yText = Text(yTextPt, str(min(yData) + (i * (max(yData) - min(yData)) / 10)))
        yText.draw(window)

        currentXCoord += xIncrement
        currentYCoord += yIncrement


# Draws set of all points from dataset onto screen
# Input: Width of window, height of window, window object, explanatory data, response data
# Output: None
# Runtime: O(n)
def drawPoints(width, height, window, xData, yData,):
    xMax = max(xData)
    xMin = min(xData)
    yMax = max(yData)
    yMin = min(yData)
    for i in range(len(xData)):
        pt = getPoint(xData[i], yData[i], xData, yData, width, height)
        # Commented out code below explicitly displays coordinates next to points
        # t = Text(pt, "(" + str(x) + ", " + str(y) + ")" )
        # t.draw(window)
        circ = Circle(pt, 3)
        circ.setFill('black')
        circ.draw(window)


# Given a set of two points from the dataset, outputs the corresponding Point
# object which is to be drawn, via mapping the dataset to the dimensions of the screen
# Input: Explanatory data point, response data point, explanatory data, response data
#        width of window, height of window
# Output: Point object
# Runtime: O(n)
def getPoint(x, y, xData, yData, width, height):
    xMax = max(xData)
    xMin = min(xData)
    yMax = max(yData)
    yMin = min(yData)
    xCoord = (x - xMin) / (xMax - xMin) * (width - 50)
    yCoord = (y - yMin) / (yMax - yMin) * (height - 50)
    if xCoord == 0:
        xCoord += 50
    if yCoord == height - 50:
        yCoord -= 50
    pt = Point(xCoord, height - 50 - yCoord)
    return pt


# Draws a line of best fit through the data
# Input: Width of window, height of window, window object,
#        explanatory data, response data
# Output: None
# Runtime: O(n)
def drawLineOfBestFit(width, height, window, xData, yData):
    model = SimpleRegression.model(xData, yData)
    slope = model[0]
    intercept = model[1]
    leftPt = getPoint(min(xData), intercept, xData, yData, width, height)
    yForMaxX = (slope * max(xData)) + intercept
    rightPt = getPoint(max(xData), yForMaxX, xData, yData, width, height)
    lineOfBestFit = Line(leftPt, rightPt)
    lineOfBestFit.draw(window)


# Sample visualization
drawSimpleRegression([5, 7, 8, 13, 7, 5, 6, 10, 5, 3, 8, 4, 5, 9, 8, 3, 4, 6, 3, 13, 3, 6, 5],
                     [6, 8, 10, 13, 6, 8, 7, 10, 6, 7, 7, 5, 7, 6, 8, 6, 5, 6, 3, 10, 5, 8, 5],)
