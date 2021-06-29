
from graphics import *
import ctypes
import SimpleRegression


# Visualizes a simple linear regression model as a set of points on a graph
# alongside the computed line of best fit
# Input: Two arrays of equal length (n)
# Output: None
def draw_simple_regression(x_data, y_data):
    if len(x_data) != len(y_data):
        raise RuntimeError("Must have one response data point per explanatory data point")

    # Set graph size based on screen resolution
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0) - 300
    height = user32.GetSystemMetrics(1) - 300
    win = GraphWin("Simple Regression", width, height)

    # Draw title
    title_pt = Point(width / 2, 25)
    title = Text(title_pt, "Simple Regression Visualization")
    subtitle_pt = Point(width / 2, 45)
    subtitle = Text(subtitle_pt, "By Albert Pimentel")
    title.draw(win)
    subtitle.draw(win)

    # Draw axes
    draw_axes(width, height, win)
    # Mark x and y axes
    label_xy_axes(width, height, win)
    # Add markers along axes
    add_markers(width, height, win, x_data, y_data)
    # Draw points on graph
    draw_points(width, height, win, x_data, y_data, )
    # Draw line of best fit
    draw_line_of_best_fit(width, height, win, x_data, y_data)
    # Close window on click and after program ends
    win.getMouse()
    win.close()


# Draws the X and Y axes of the graph
# Input: Width of window, height of window, window object
# Output: None
def draw_axes(width, height, window):
    top_left = Point(50, 50)
    bottom_left = Point(50, height - 50)
    bottom_right = Point(width - 50, height - 50)
    line1 = Line(top_left, bottom_left)
    line2 = Line(bottom_left, bottom_right)
    line1.draw(window)
    line2.draw(window)


# Labels the X and Y axes of the graph
# Input: Width of window, height of window, window object
# Output: None
def label_xy_axes(width, height, window):
    # Mark x and y axes
    x_label_pt = Point(40, 50)
    x_label = Text(x_label_pt, "y")
    y_label_pt = Point(width - 50, height - 40)
    y_label = Text(y_label_pt, "x")
    x_label.draw(window)
    y_label.draw(window)


# Adds 10 markers along the axes of the graph to give a better idea
# of where points lie
# Input: Width of window, height of window, window object, explanatory data, response data
# Output: None
def add_markers(width, height, window, x_data, y_data):
    # Add 10 markers along each axis
    x_increment = (width - 100) / 10
    y_increment = (height - 100) / -10
    current_x_coord = 50
    current_y_coord = height - 50
    for i in range(10):
        # Draw marker on x-axis
        x_pt1 = Point(current_x_coord, height - 60)
        x_pt2 = Point(current_x_coord, height - 40)
        x_line = Line(x_pt1, x_pt2)
        x_line.draw(window)
        # Place corresponding number below marker
        x_text_pt = Point(current_x_coord, height - 30)
        x_text = Text(x_text_pt, str(min(x_data) + (i * (max(x_data) - min(x_data)) / 10)))
        x_text.draw(window)

        # Draw marker on y-axis
        y_pt1 = Point(40, current_y_coord)
        y_pt2 = Point(60, current_y_coord)
        y_line = Line(y_pt1, y_pt2)
        y_line.draw(window)
        # Place corresponding number left of marker
        y_text_pt = Point(25, current_y_coord)
        y_text = Text(y_text_pt, str(min(y_data) + (i * (max(y_data) - min(y_data)) / 10)))
        y_text.draw(window)

        current_x_coord += x_increment
        current_y_coord += y_increment


# Draws set of all points from dataset onto screen
# Input: Width of window, height of window, window object, explanatory data, response data
# Output: None
def draw_points(width, height, window, x_data, y_data, ):
    x_max = max(x_data)
    x_min = min(x_data)
    y_max = max(y_data)
    y_min = min(y_data)
    for i in range(len(x_data)):
        pt = get_point(x_data[i], y_data[i], x_data, y_data, width, height)
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
def get_point(x, y, x_data, y_data, width, height):
    x_max = max(x_data)
    x_min = min(x_data)
    y_max = max(y_data)
    y_min = min(y_data)
    x_coord = (x - x_min) / (x_max - x_min) * (width - 50)
    y_coord = (y - y_min) / (y_max - y_min) * (height - 50)
    if x_coord == 0:
        x_coord += 50
    if y_coord == height - 50:
        y_coord -= 50
    pt = Point(x_coord, height - 50 - y_coord)
    return pt


# Draws a line of best fit through the data
# Input: Width of window, height of window, window object,
#        explanatory data, response data
# Output: None
def draw_line_of_best_fit(width, height, window, x_data, y_data):
    model = SimpleRegression.model(x_data, y_data)
    slope = model[0]
    intercept = model[1]
    left_pt = get_point(min(x_data), intercept, x_data, y_data, width, height)
    y_for_max_x = (slope * max(x_data)) + intercept
    right_pt = get_point(max(x_data), y_for_max_x, x_data, y_data, width, height)
    line_of_best_fit = Line(left_pt, right_pt)
    line_of_best_fit.draw(window)


# Sample visualization
draw_simple_regression([5, 7, 8, 13, 7, 5, 6, 10, 5, 3, 8, 4, 5, 9, 8, 3, 4, 6, 3, 13, 3, 6, 5],
                       [6, 8, 10, 13, 6, 8, 7, 10, 6, 7, 7, 5, 7, 6, 8, 6, 5, 6, 3, 10, 5, 8, 5], )
