from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class create():
    register_txt_xpath = "//a[@title='Log in to your customer account']"
    email_txt_xpath = "//input[@id='email_create']"
    create_button_xpath = "//span[normalize-space()='Create an account']"
    confirm_msg_xpath = "//h3[@class='page-subheading']"
    clk_male_xpath="//label[@for='id_gender1']"
    clk_female_xpth="//label[@for='id_gender2']"
    txt_firstname_xpath="//input[@id='customer_firstname']"
    txt_lastname_xpath="//input[@id='customer_lastname']"
    txt_password_xpath="//input[@id='passwd']"
    drop_date_xpath="//select[@id='days']"
    drop_month_xpath="//select[@id='months']"
    drop_year_xpath="//select[@id='years']"
    clk_newspaper_xpath="//input[@id='newsletter']"
    clk_submit_xpath="//span[normalize-space()='Register']"
    txt_confirm_xpath="//h1[@class='page-heading']"

    def __init__(self,driver):
        self.driver=driver

    def signin(self):
        self.driver.find_element(By.XPATH, self.register_txt_xpath).click()

    def email(self, usremail):
        self.driver.find_element(By.XPATH, self.email_txt_xpath).send_keys(usremail)

    def create(self):
        self.driver.find_element(By.XPATH, self.create_button_xpath).click()

    def setmale(self):
        self.driver.find_element(By.XPATH,self.clk_male_xpath)

    def setfemale(self):
        self.driver.find_element(By.XPATH,self.clk_female_xpth).click()

    def setfirstname(self,fname):
        self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(fname)

    def setlastname(self,lname):
        self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(lname)

    def setpassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(pwd)

    def setdate(self,day):
        self.dobday=Select(self.driver.find_element(By.XPATH,self.drop_date_xpath))
        self.dobday.select_by_value(day)

    def setmonth(self,month):
        self.dobmonth=Select(self.driver.find_element(By.XPATH,self.drop_month_xpath))
        self.dobmonth.select_by_value(month)

    def setyear(self,year):
        self.dobyear=Select(self.driver.find_element(By.XPATH,self.drop_year_xpath))
        self.dobyear.select_by_value(year)

    def setnewspaper(self):
        self.driver.find_element(By.XPATH,self.clk_newspaper_xpath).click()

    def msgConfirm(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_confirm_xpath).text
        except:
            None