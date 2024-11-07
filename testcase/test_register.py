import os
import time

from pageobjects.signup import signup


class Test_register():
    baseURL="http://www.automationpractice.pl/index.php"

    def test_signup(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.sp=signup(self.driver)
        self.sp.signin()
        self.sp.email("shan@yahoo.com")
        self.sp.create()

        self.check=self.sp.confirmMsg()
        if self.check == "Your personal information":
           assert True
        else:
           self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots/test_registernew1.png")


time.sleep(6)

#test

