# -*- coding: utf-8 -*-

from robot.libraries.BuiltIn import BuiltIn

class ConnectionManagement:

    def __init__(self):
        self._bi = BuiltIn()

    #KeyWord
    
    def t_close_application_session(self):
        """ปิดแอพปัจจุบันและปิดเซสชัน"""
        
    #PRIVATE_FUNCTION
        
    def _current_application(self):
        """
        คืนค่าอินสแตนซ์ของแอปพลิเคชันปัจจุบัน
        จาก AppiumFlutterLibrary
        """
        return self._bi.get_library_instance('AppiumFlutterLibrary')._current_application()
        