from pageobjects.signin import myAccount


class Test_signinAccount():
    baseURL="http://www.automationpractice.pl/index.php"

    def test_login(self,setup):
         self.driver=setup
         self.driver.get(self.baseURL)
         self.driver.maximize_window()
         self.driver.implicitly_wait(10)

         self.ma=myAccount(self.driver)
         self.ma.signin()
         self.ma.setemail("loga@gmail.com")
         self.ma.setpwd("shobana_4u")
         self.ma.clicksignin()
         self.msgconfirm=self.ma.confirm()

         if self.msgconfirm == "My account":
              assert True

         else:
              assert False

