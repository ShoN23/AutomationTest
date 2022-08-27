from selenium import webdriver
import pytest
from unittest import TestCase
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as cond

class MessengerTests(TestCase):
    driver = None
    options = Options()

    _gr_name = 'test_group1'
    _gr_description = 'automation test'
    _msg = 'Hello everyone!'

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #cls.options.platform_name = 'Windows 11'
        cls.options.add_experimental_option("useAutomationExtension", 'false')
        cls.options.add_experimental_option("excludeSwitches", ['enable-automation'])
        cls.driver.maximize_window()
        cls.driver.get("https://www.wehago.com/landing/mobile/ko/home/")

    @pytest.mark.order(1)
    def test_login(self):
        wait(self.driver, 10).until(cond.presence_of_element_located((By.ID, 'login'))).click()
        self.driver.find_element(By.ID, 'inputId').send_keys('testsw5')
        self.driver.find_element(By.ID, 'inputPw').send_keys('1q2w3e4r')
        self.driver.find_element(By.CLASS_NAME, 'WSC_LUXButton').click()

        try:
            if wait(self.driver, 5).until(cond.presence_of_element_located((By.CLASS_NAME, 'duplicate_login'))):
                self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div/div[5]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/button[2]').click()
        except:
            pass

        assert wait(self.driver, 5).until(
            cond.presence_of_element_located((By.CLASS_NAME, 'tit'))).text == '기업에 필요한 다양한 업무환경 WEHAGO'

    @pytest.mark.order(2)
    def test_Messenger(self):
        wait(self.driver, 10).until(cond.presence_of_element_located((By.ID, 'MAIN-SVC_communication-sp'))).click()
        #assert wait(self.driver, 5).until(cond.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[1]/div[1]/ul/li[1]/a/span'))).text == '대화방'

    @pytest.mark.order(3)
    def test_Creat_newchat(self):
        wait(self.driver, 30).until(cond.presence_of_element_located((By.CLASS_NAME, 'button_new'))).click()
        # group chat
        wait(self.driver, 5).until(cond.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div/ul/li[1]/a'))).click()

        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/input').send_keys(self.__class__._gr_name)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div/div/input').send_keys(self.__class__._gr_description)
        #   Visibility check
        wait(self.driver, 5).until(cond.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/div/div/div/div[2]/div[3]/div/div[1]/span/span'))).click()

        # Navigation target
        wait(self.driver, 5).until(cond.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/div/div/div/div[2]/div[4]/div/div[2]/button'))).click()
        # Adding members
        wait(self.driver, 5).until(cond.presence_of_element_located((By.ID, 'memberbx_0'))).click()
        self.driver.find_element(by=By.XPATH,
                            value='/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div/button[1]').click()
        self.driver.find_element(by=By.ID, value='memberbx_4').click()
        self.driver.find_element(by=By.XPATH,
                            value='/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div/button[1]').click()
        self.driver.find_element(by=By.ID, value='memberbx_5').click()
        self.driver.find_element(by=By.XPATH,
                            value='/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div/button[1]').click()
        self.driver.find_element(by=By.ID, value='memberbx_2').click()
        wait(self.driver, 10).until(cond.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div/button[1]'))).click()
        # Confirm to create group
        wait(self.driver, 10).until(cond.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[3]/button[2]'))).click()
        # Start Conversation
        self.driver.implicitly_wait(10)
        wait(self.driver, 10).until(cond.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/div/div/div/div[2]/div[5]/div/button[2]'))).click()

        # Sending message
        self.driver.implicitly_wait(10)
        # wait(self.driver, 5).until(cond.presence_of_element_located((By.ID, 'mentiony-content-cs9u3w'))).send_keys(self.__class__._msg)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[3]/div[2]/div[2]/div/div[1]/div[2]').send_keys(self.__class__._msg)
        wait(self.driver, 10).until(cond.presence_of_element_located((By.CLASS_NAME, 'chat_submit'))).click()
       # self.driver.find_element(by=By.CLASS_NAME, value='chat_submit').click()
        # Chat room list
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.ID, value='roomSearch').click()
        # joining test_group
        self.driver.implicitly_wait(10)
        wait(self.driver, 10).until(cond.presence_of_element_located((By.CSS_SELECTOR, '#BODY_CLASS > div.snbnext > div > div > div > div > div > div:nth-child(1) > div:nth-child(3) > div._isDialog.WSC_LUXDialog > div:nth-child(2) > div > div > div:nth-child(1) > div.dialog_wrap > div > div > div.dialog_data_area.noline.mgt15 > div > div > ul > li:nth-child(2) > div.item_button > button'))).click()
        wait(self.driver, 10).until(cond.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[3]/div[2]/div[2]/div/div[1]/div[2]'))).send_keys(self.__class__._msg)

        wait(self.driver, 10).until(cond.presence_of_element_located((By.CLASS_NAME, 'chat_submit'))).click()

        # Add group to favourite
        self.driver.find_element(by=By.CSS_SELECTOR, value='#roomId_X5zG2IIBXVXQfnUuUpaz > div > div > div > div:nth-child(1) > button').click()
        self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div/div/ul/li[1]/a').click()
        # Removing from favourite
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div[2]/div[1]/div[3]/ul/li/div/div/div/div[1]/button').click()
        self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div/div/ul/li[1]/a').click()
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[4]/div[2]/div/div/div[2]/button[2]').click()

        #1:1 message
        wait(self.driver, 10).until(cond.presence_of_element_located((By.XPATH, '//*[@id="BODY_CLASS"]/div[3]/div/div/div/div/div/div[1]/div[3]/div[1]/div[1]/ul/li[2]/a'))).click()
        # sent message on menu
        wait(self.driver, 10).until(cond.presence_of_element_located((By.CLASS_NAME, 'button_new'))).click()
        # finding someone
        wait(self.driver, 10).until(cond.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div/div[1]/dl/dd[2]/button'))).click()
        # going to organization chart
        wait(self.driver, 10).until(cond.presence_of_element_located((By.ID, 'tab_2'))).click()
        wait(self.driver, 10).until(cond.presence_of_element_located((By.ID, 'memberbx_0'))).click()
        wait(self.driver, 10).until(cond.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div/button[1]'))).click()
        wait(self.driver, 10).until(cond.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[3]/button[2]'))).click()
        # sending message
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.ID, value='msgTextArea').send_keys(self.__class__._msg)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[3]/div/div[3]/button').click()
        # deleting message
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div[1]/div[2]/div/div[2]/button[4]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div/div/div/div[4]/div[2]/div/div/div[2]/button[2]').click()


if __name__ =='__main__':
    pytest.main()

