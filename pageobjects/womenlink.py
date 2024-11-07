from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class womenlink():
       clk_womwnlink_xpath="//a[@title='Women']"
       clk_summer_absxpath="/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[6]/ul[1]/li[1]/ul[1]/li[2]/ul[1]/li[3]/a[1]"
       # clk_img_absxpath="/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[2]/div[1]/div[1]/div[1]/a[1]/img[1]"
       # clk_more_xpath="/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[2]/ul[1]/li[2]/div[1]/div[2]/div[2]/a[1]/span[1]"
       # clk_white_xpath="//a[@id='color_8']"
       # clk_quantityplus_xpath="//i[@class='icon-plus']"
       # clk_quantityminus_xpath="//i[@class='icon-minus']"
       # drop_size_xpath="//select[@id='group_1']"
       # clk_addtocart_xpath="//span[normalize-space()='Add to cart']"

       def __init__(self, driver):
           self.driver = driver

       def setwomen(self):
            self.driver.find_element(By.XPATH,self.clk_womwnlink_xpath).click()

       def  setsummer(self):
            self.driver.find_element(By.XPATH,self.clk_summer_absxpath).click()


       # def setimage(self):
       #      self.driver.find_element(By.XPATH,self.clk_img_absxpath).click()
       #
       #
       # def setwhite(self):
       #      self.driver.find_element(By.XPATH,self.clk_white_xpath).click()
       #
       # def setquantityPlus(self):
       #      self.driver.find_element(By.XPATH,self.clk_quantityplus_xpath).click()
       #
       # def setsize(self,size):
       #      self.size=Select(self.driver.find_element(By.XPATH,self.drop_size_xpath))
       #      self.size.select_by_visible_text(size)
       #
       # def setaddTocart(self):
       #      self.driver.find_element(By.XPATH,self.clk_addtocart_xpath).click()
       #
