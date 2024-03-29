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
    
    def native_close_application_session(self):
        """Close Application And Quit Seesion

        =========================================================
        
        ปิดแอพปัจจุบันและปิดเซสชัน"""

    def native_background_application(self, seconds=5):
        """
        Puts the application in the background on the device for a certain
        duration.

        =========================================================

        วางแอปพลิเคชันไว้ในพื้นหลังของอุปกรณ์เป็นระยะเวลาหนึ่ง.
        """
        self._current_application().background_app(seconds)
        
    def native_activate_application(self, app_id):
        """
        Activates the application if it is not running or is running in the background.
        Args:
         - app_id - BundleId for iOS. Package name for Android.

        New in AppiumLibrary v2

        =========================================================

        
        เปิดใช้งานแอปพลิเคชันหากมันไม่ได้รันอยู่หรือรันอยู่ในพื้นหลัง
        อาร์กิวเมนต์:
        - app_id - BundleId สำหรับ iOS, ชื่อแพ็คเกจสำหรับ Android.
        """
        self._current_application().activate_app(app_id)

    def native_terminate_application(self, app_id):
        """
        Terminate the given app on the device

        Args:
         - app_id - BundleId for iOS. Package name for Android.

        New in AppiumLibrary v2

        =========================================================
        
        ยุติแอปพลิเคชันที่กำหนดไว้บนอุปกรณ์แต่ยัง active อยู่ในระบบ
        สามารถเปิดต่อได้

        อาร์กิวเมนต์:  

        app_id - BundleId สำหรับ iOS, ชื่อแพ็คเกจสำหรับ Android.
        ใหม่ใน AppiumLibrary เวอร์ชัน 2
        """
        return self._current_application().terminate_app(app_id)
    #PRIVATE_FUNCTION
        
    def _current_application(self):
        """Return the instance of the current application
        From AppiumFlutterLibrary

        =========================================================

        คืนค่าอินสแตนซ์ของแอปพลิเคชันปัจจุบัน
        จาก AppiumFlutterLibrary
        """
        return cache_app.get_library_instance('AppiumFlutterLibrary')._current_application()
        # return self._bi.get_library_instance('AppiumFlutterLibrary')._current_application()
        