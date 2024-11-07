from selenium.webdriver.common.by import By


class myAccount():
    click_signin_xpath="//a[@title='Log in to your customer account']"
    txt_email_xpath="//input[@id='email']"
    txt_passWord_xpath="//input[@id='passwd']"
    button_signin_xpath="//span[normalize-space()='Sign in']"
    txt_confirm_xpath="//h1[@class='page-heading']"

    def __init__(self,driver):
        self.driver=driver

    def signin(self):
        self.driver.find_element(By.XPATH,self.click_signin_xpath).click()

    def setemail(self,uemail):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(uemail)

    def setpwd(self,upwd):
        self.driver.find_element(By.XPATH,self.txt_passWord_xpath).send_keys(upwd)

    def clicksignin(self):
        self.driver.find_element(By.XPATH,self.button_signin_xpath).click()

    def confirm(self):

        try:
            return self.driver.find_element(By.XPATH,self.txt_confirm_xpath).text
        except:
            None


