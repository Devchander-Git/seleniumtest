from pageobjects.signin import myAccount
from pageobjects.womenlink import womenlink
from utlities.readProperties import ReadConfig


class Test_womenLink():
    baseURL=ReadConfig.getApplicationURL()


    def test_selectdress(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


        self.ma=myAccount(self.driver)
        self.ma.signin()
        self.ma.setemail("loga@gmail.com")
        self.ma.setpwd("shobana_4u")
        self.ma.clicksignin()

        self.wl=womenlink(self.driver)
        self.wl.setwomen()
        self.wl.setsummer()
        # self.wl.setimage()
        # self.wl.setwhite()
        # self.wl.setquantityPlus()
        # self.wl.setsize("1")
        # self.wl.setaddTocart()

