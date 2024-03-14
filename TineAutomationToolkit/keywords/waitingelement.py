# -*- coding: utf-8 -*-

import time
import robot

from .controlelement import ControlElement
from AppiumLibrary.keywords._applicationmanagement import _ApplicationManagementKeywords

conelement = ControlElement()

class WaitingElement:
    
    def __init__(self):
        #เนื่องจากปัญหาเรื่องโครงสร้าง structure เลยยังไม่สามารถใช้ได้
        # self._ce = ControlElement()
        self._af_amk = _ApplicationManagementKeywords()
        self._timeout_in_secs = float(5)

        

    #KeyWord

    def t_wait_element_is_visible(self,locator, timeout=None, error=None):
        """Waits until element specified with `locator` is visible.

        Wait Until Element Is Visible:
            รอจนกว่าองค์ประกอบ (element) ที่ระบุจะปรากฏในหน้าแอพพลิเคชันและสามารถมองเห็นได้
            ถ้าองค์ประกอบไม่ปรากฏหรือไม่สามารถมองเห็นได้ภายในระยะเวลาที่กำหนด, การทดสอบจะล้มเหลว
            ใช้เมื่อคุณต้องการรอให้องค์ประกอบมองเห็นได้จริงก่อนที่จะดำเนินการต่อ

            
        """

        def check_visibility():
            visible = conelement._is_visible(locator)
            if visible:
                return
            elif visible is None:
                return error or "Element locator '%s' did not match any elements after %s" % (locator, self._format_timeout(timeout))
            else:
                return error or "Element '%s' was not visible in %s" % (locator, self._format_timeout(timeout))
        
        self._wait_until_no_error(timeout, check_visibility)

    def t_wait_until_page_contains_element(self, locator, timeout=None, error=None):
        """Waits until element specified with `locator` appears on current page.

        Fails if `timeout` expires before the element appears. See
        `introduction` for more information about `timeout` and its
        default value.

        `error` can be used to override the default error message.

        See also `Wait Until Page Contains`,
        `Wait Until Page Does Not Contain`
        `Wait Until Page Does Not Contain Element`
        and BuiltIn keyword `Wait Until Keyword Succeeds`.

        Wait Until Page Contains Element:
        รอจนกว่าองค์ประกอบ (element) ที่ระบุจะปรากฏในหน้าแอพพลิเคชัน แต่ไม่จำเป็นต้องมองเห็นได้
        ถ้าองค์ประกอบไม่ปรากฏในหน้าภายในระยะเวลาที่กำหนด, การทดสอบจะล้มเหลว
        ใช้เมื่อคุณต้องการรอให้องค์ประกอบมีอยู่ใน DOM ของหน้าเว็บ แต่ไม่จำเป็นต้องมองเห็นได้จริง
        """
        if not error:
            error = "Element '%s' did not appear in <TIMEOUT>" % locator
        self._wait_until(timeout, error, conelement._is_element_present, locator)
    
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

    
    def _wait_until(self, timeout, error, function, *args):
        error = error.replace('<TIMEOUT>', self._format_timeout(timeout))

        def wait_func():
            return None if function(*args) else error

        self._wait_until_no_error(timeout, wait_func)