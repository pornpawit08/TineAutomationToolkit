# -*- coding: utf-8 -*-

import ast

from AppiumLibrary.locators import ElementFinder
from AppiumLibrary.keywords._logging import _LoggingKeywords
from .connectionmanagement import ConnectionManagement
from selenium.webdriver.remote.webelement import WebElement

def isstr(s):
    return isinstance(s, str)


class ControlElement:

    def __init__(self):
        self._element_finder_t = ElementFinder()
        self._co = ConnectionManagement
        self._log = _LoggingKeywords

    #KeyWord
    
        #Switch_Mode
        
    def t_switch_mode(self,mode):
        """
        Switch Mode ระหว่าง Flutter และ NATIVE_APP
        จำเป็นต้อง Run ด้วย automationname : Flutter เท่านั้น
        """
        driver = self._co._current_application()

        if mode == 'NATIVE_APP':
            driver.switch_to.context('NATIVE_APP')
        if mode == 'FLUTTER':
            driver.switch_to.context('FLUTTER')
 
        #Click_Element
    def t_click_element(self,locator):
        """กด click หรือ tap element
        ตาม locator ที่ระบุเข้ามา
        """
        self._log._info("Clicking element '%s'." % locator)
        self._element_find_t(locator, True , True).click()
        
    #PRIVATE_FUNCTION
        
    def _element_find_t(self, locator, first_only, required, tag=None):
        application = self._co._current_application()
        elements = None
        if isstr(locator):
            _locator = locator
            elements = self._element_finder_t.find(application, _locator, tag)
            if required and len(elements) == 0:
                raise ValueError("Element locator '" + locator + "' did not match any elements.")
            if first_only:
                if len(elements) == 0: return None
                return elements[0]
        elif isinstance(locator, WebElement):
            if first_only:
                return locator
            else:
                elements = [locator]
        # do some other stuff here like deal with list of webelements
        # ... or raise locator/element specific error if required
        return elements
    
    def _is_visible(self, locator):
        element = self._element_find_t(locator, True, False)
        if element is not None:
            return element.is_displayed()
        return None