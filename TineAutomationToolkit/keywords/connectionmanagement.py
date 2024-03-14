# -*- coding: utf-8 -*-

import robot

from robot.libraries.BuiltIn import BuiltIn

cache_app = BuiltIn()

class ConnectionManagement:

    def __init__(self):
        #เนื่องจากปัญหาเรื่องโครงสร้าง structure เลยยังไม่สามารถใช้ได้
        # self._bi = BuiltIn()
        pass
    #KeyWord
    
    def t_close_application_session(self):
        """ปิดแอพปัจจุบันและปิดเซสชัน"""

    def t_background_application(self, seconds=5):
        """
        Puts the application in the background on the device for a certain
        duration.
        """
        self._current_application().background_app(seconds)
        
    def t_activate_application(self, app_id):
        """
        Activates the application if it is not running or is running in the background.
        Args:
         - app_id - BundleId for iOS. Package name for Android.

        New in AppiumLibrary v2
        """
        self._current_application().activate_app(app_id)

    def t_terminate_application(self, app_id):
        """
        Terminate the given app on the device

        Args:
         - app_id - BundleId for iOS. Package name for Android.

        New in AppiumLibrary v2
        """
        return self._current_application().terminate_app(app_id)
    #PRIVATE_FUNCTION
        
    def _current_application(self):
        """
        คืนค่าอินสแตนซ์ของแอปพลิเคชันปัจจุบัน
        จาก AppiumFlutterLibrary
        """
        return cache_app.get_library_instance('AppiumFlutterLibrary')._current_application()
        # return self._bi.get_library_instance('AppiumFlutterLibrary')._current_application()
        