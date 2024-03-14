# -*- coding: utf-8 -*-

from .controlelement import ControlElement
from .connectionmanagement import ConnectionManagement

conelement = ControlElement()
cache_app = ConnectionManagement()

class Scroll:

    def __init__(self):
        pass


    def t_scroll(self, start_locator, end_locator):
        """
        Scrolls from one element to another
        Key attributes for arbitrary elements are `id` and `name`. See
        `introduction` for details about locating elements.
        """
        el1 = conelement._element_find_t(start_locator, True, True)
        el2 = conelement._element_find_t(end_locator, True, True)
        driver = cache_app._current_application()
        driver.scroll(el1, el2)

    def swipe(self, start_x, start_y, offset_x, offset_y, duration=1000):
        """
        Swipe from one point to another point, for an optional duration.

        Args:
         - start_x - x-coordinate at which to start
         - start_y - y-coordinate at which to start
         - offset_x - x-coordinate distance from start_x at which to stop
         - offset_y - y-coordinate distance from start_y at which to stop
         - duration - (optional) time to take the swipe, in ms.

        Usage:
        | Swipe | 500 | 100 | 100 | 0 | 1000 |

        _*NOTE: *_
        Android 'Swipe' is not working properly, use ``offset_x`` and ``offset_y`` as if these are destination points.
        """
        x_start = int(start_x)
        x_offset = int(offset_x)
        y_start = int(start_y)
        y_offset = int(offset_y)
        driver = cache_app._current_application()
        driver.swipe(x_start, y_start, x_offset, y_offset, duration)
