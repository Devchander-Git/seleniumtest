from selenium.webdriver.common.by import By


class signup():
    register_txt_xpath="//a[@title='Log in to your customer account']"
    email_txt_xpath="//input[@id='email_create']"
    create_button_xpath="//span[normalize-space()='Create an account']"
    confirm_msg_xpath="//h3[@class='page-subheading']"

    def __init__(self,driver):
      self.driver=driver

    def signin(self):
        self.driver.find_element(By.XPATH,self.register_txt_xpath).click()

    def email(self,usremail):
        self.driver.find_element(By.XPATH,self.email_txt_xpath).send_keys(usremail)

    def create(self):
        self.driver.find_element(By.XPATH,self.create_button_xpath).click()

    def confirmMsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.confirm_msg_xpath).text
        except:
            None





