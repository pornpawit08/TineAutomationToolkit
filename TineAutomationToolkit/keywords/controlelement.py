# -*- coding: utf-8 -*-

from AppiumLibrary.locators import ElementFinder
from .connectionmanagement import ConnectionManagement

class ControlElement:

    def __init__(self):
        self._element_finder_t = ElementFinder()
        self._co = ConnectionManagement

    #KeyWord
    
        #Switch_Mode

    def t_switch_mode(self,mode):
        """
        Switch Mode ระหว่าง Flutter และ NATIVE_APP
        จำเป็นต้อง Run ด้วย automationname : Flutter เท่านั้น
        """
        driver = self._co._current_application

        if mode == 'NATIVE_APP':
            driver.switch_to.context('NATIVE_APP')
        if mode == 'FLUTTER':
            driver.switch_to.context('FLUTTER')

        
    #PRIVATE_FUNCTION
        