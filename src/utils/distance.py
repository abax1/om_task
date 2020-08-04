import math
from src.config.constants import X_AXIS, Y_AXIS, X_MAP, Y_MAP
from src.utils.logger import logger


def calculate_distance(point_a: (str, int), point_b: (str, int)) -> float:
    """Take a value e.g. x=A0 y=J5 and calculate the distance between the two points in nautical miles."""

    # Validate the input
    if point_a is None or point_b is None:
        raise ValueError("point_a or point_b cannot be None!")
    if point_a[0].upper() not in X_AXIS:
        raise ValueError("point_a x value must be in [A,B,C,D,E,F,G,H,I,J,K]")
    if point_a[1] not in Y_AXIS:
        raise ValueError("point_a y value must be in [0,1,2,3,4,5,6,7,8,9]")
    if point_b[0].upper() not in X_AXIS:
        raise ValueError("point_b x value must be in [A,B,C,D,E,F,G,H,I,J,K]")
    if point_b[1] not in Y_AXIS:
        raise ValueError("point_b y value must be in [0,1,2,3,4,5,6,7,8,9]")

    # Extract the values from the tuples
    x1, y1 = point_a
    x2, y2 = point_b

    logger.debug("point_a={},{}".format(x1, y1))
    logger.debug("point_b={},{}".format(x2, y2))

    # Convert the x and y values to nautical miles map
    x1 = X_MAP.get(x1.upper(), None)
    y1 = Y_MAP.get(y1, None)
    logger.debug("point_a={},{}".format(x1, y1))
    x2 = X_MAP.get(x2.upper(), None)
    y2 = Y_MAP.get(y2, None)
    logger.debug("point_b={},{}".format(x2, y2))

    # Calculate the distance between the two points.
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance



