# -*- coding: utf-8 -*-

import time
import robot

from .controlelement import ControlElement
from AppiumLibrary.keywords._applicationmanagement import _ApplicationManagementKeywords

class WaitingElement:
    
    def __init__(self):
        self._ce = ControlElement
        self._timeout_in_secs = float(5)
        self._af_amk = _ApplicationManagementKeywords

        

    #KeyWord

    def t_wait_element_is_visible(self,locator, timeout=None, error=None):
        """Waits until element specified with `locator` is visible."""

        def check_visibility():
            visible = self._ce._is_visible(locator)
            if visible:
                return
            elif visible is None:
                return error or "Element locator '%s' did not match any elements after %s" % (locator, self._format_timeout(timeout))
            else:
                return error or "Element '%s' was not visible in %s" % (locator, self._format_timeout(timeout))
        
        self._wait_until_no_error(timeout, check_visibility)

    
    #PRIVATE_FUNCTION
        
    def _format_timeout(self, timeout):
        timeout = robot.utils.timestr_to_secs(timeout) if timeout is not None else self._timeout_in_secs
        return robot.utils.secs_to_timestr(timeout)
    
    def _wait_until_no_error(self, timeout, wait_func, *args):
        timeout = robot.utils.timestr_to_secs(timeout) if timeout is not None else self._timeout_in_secs
        maxtime = time.time() + timeout
        while True:
            timeout_error = wait_func(*args)
            if not timeout_error:
                return
            if time.time() > maxtime:
                self._af_amk.log_source()
                raise AssertionError(timeout_error)
            time.sleep(0.2)