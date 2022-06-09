import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Test_NetflixTEST:
    @pytest.fixture
    def test_setUP(self):

        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()

        yield
        print("success")
        driver.close()
        driver.quit()


    def test_loginFunctionality(self,test_setUP):
        driver.get("https://www.netflix.com/bd/")
        driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a').click()
        time.sleep(3)
        driver.find_element(By.NAME,"userLoginId").send_keys("4rough07@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID,"id_password" ).send_keys("wq12!@")
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
        time.sleep(3)


