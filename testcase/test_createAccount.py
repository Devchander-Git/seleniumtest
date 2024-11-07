import os.path

from pageobjects.createPage import create


class Test_createAccount():
    baseURL="http://www.automationpractice.pl/index.php"

    def test_account(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.ca=create(self.driver)
        self.ca.signin()
        self.ca.email("shan@yahoo.com")
        self.ca.create()
        self.ca.setmale()
        self.ca.setfemale()
        self.ca.setfirstname("Dev")
        self.ca.setlastname("Chander")
        self.ca.setpassword("swarncse99*")
        self.ca.setdate("2")
        self.ca.setmonth("4")
        self.ca.setyear("2021")
        self.ca.setnewspaper()
        self.confirm=self.ca.msgConfirm()

        if self.confirm == "My account":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots//test_createAccount.png")
            assert False