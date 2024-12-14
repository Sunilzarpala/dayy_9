# import time
#
# from selenium import webdriver
# import pytest
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
#
# class Test_credkart_login_next_Checkout():
    # @pytest.mark.skip
    # def test_login_credkart_001(self,setup):
    #     self.driver = setup
    #     # driver= webdriver.Chrome()
    #     # driver.maximize_window()
    #     self.driver.get("https://automation.credence.in/login")
    #     self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys("Credencetest@test.com")
    #     self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/input[1]").send_keys("Credence@123")
    #     self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/button[1]").click()
    #     try:
    #         self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/h2[1]")
    #         self.driver.save_screenshot("C:\\PYTHON PRACTICE\\seleniumDAY7\\Screen\\login_pass.png")
    #         self.driver.close()
    #         assert True
    #
    #     except:
    #         self.driver.save_screenshot("C:\\PYTHON PRACTICE\\seleniumDAY7\\Screen\\login_fail.png")
    #         self.driver.close()
    #         assert False


    # @pytest.mark.sun
    # def test_credkart_checkout_002(self,setup):
    #     # driver = webdriver.Chrome()
    #     # driver.maximize_window()
    #     self.driver= setup
    #     self.driver.implicitly_wait(200)
    #     self.driver.get("https://automation.credence.in/login")
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys("Credencetest@test.com")
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/input[1]").send_keys("Credence@123")
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/button[1]").click()
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[1]/a[2]/h3[1]").click()
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[5]").click()
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[2]").click()
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("sunil")
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys("zarpala")
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("9822549998")
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/textarea[1]").send_keys("pune karvenagar")
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]/div[1]/input[1]").send_keys("411052")
    #     state= Select(self.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/select[1]"))
    #     state.select_by_index(1)
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/input[1]").send_keys("sunil")
    #     time.sleep(10)
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/input[1]").send_keys("043")
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/input[1]").send_keys("5281")
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/input[1]").send_keys("0370")
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/input[1]").send_keys("4891")
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/input[1]").send_keys("6168")
    #     year = Select(self.driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[4]/select[2]"))
    #     year.select_by_index(2)
    #     month = Select(self.driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[4]/select[1]"))
    #     month.select_by_index(2)
    #     self.driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/button[1]").click()
    #     try:
    #         self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]")
    #         print(self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]").text)
    #         self.driver.save_screenshot("C:\\PYTHON PRACTICE\\seleniumDAY7\\Screen\\Checkout_pass.png")
    #         time.sleep(3)
    #
    #         self.driver.close()
    #         assert True
    #     except:
    #         time.sleep(2)
    #         print("order is unsuccessful please try agin!!")
    #         self.driver.save_screenshot("C:\\PYTHON PRACTICE\\seleniumDAY7\\Screen\\Checkout_fail.png")
    #         self.driver.close()
    #         assert False
    #







