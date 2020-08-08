from datetime import time

from src.utils.logger import logger


def get_timestep(t: time = None) -> int:
    logger.debug("input_time={}".format(t))
    # Validate the input
    if t is None:
        raise ValueError("input_time cannot be None!")

    if time(0, 0) <= t <= time(1, 0):
        return 0
    if time(1, 0) < t <= time(2, 0):
        return 1
    if time(2, 0) < t <= time(3, 0):
        return 2
    if time(3, 0) < t <= time(4, 0):
        return 3
    if time(4, 0) < t <= time(5, 0):
        return 4
    if time(5, 0) < t <= time(6, 0):
        return 5
    if time(6, 0) < t <= time(7, 0):
        return 6
    if time(7, 0) < t <= time(8, 0):
        return 7
    if time(8, 0) < t <= time(9, 0):
        return 8
    if time(9, 0) < t <= time(10, 0):
        return 9

    return 9  # else for all others then return 9


def convert_float_to_time(time_value: float) -> time:
    minutes = time_value * 60
    hours, minutes = divmod(minutes, 60)
    return time(int(hours), int(minutes))