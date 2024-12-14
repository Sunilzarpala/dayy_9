# import time
#
# from selenium import webdriver
# import pytest
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
#
#
#
# class Test_credkart_login_params():
#     # @pytest.mark.skip
#     def test_login_credkart_params_001(self,setup, getDataForLogin):
#         self.driver = setup
#         # driver= webdriver.Chrome()
#         # driver.maximize_window()
#         self.driver.get("https://automation.credence.in/login")
#         self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys(getDataForLogin[0])
#         self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/input[1]").send_keys(getDataForLogin[1])
#         self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/button[1]").click()
#         try:
#             self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/h2[1]")
#             print('login sucessful')
#             self.driver.save_screenshot("C:\\PYTHON PRACTICE\\seleniumDAY7\\Screen\\"+ getDataForLogin[0]+getDataForLogin[1]+"_"+"loginp_param.png")
#
#             assert True
#             self.driver.close()
#
#
#         except:
#             print("Login unsuccessful")
#             self.driver.save_screenshot("C:\\PYTHON PRACTICE\\seleniumDAY7\\Screen\\"+ getDataForLogin[0]+getDataForLogin[1]+"_"+"loginp_param.png")
#             assert False
#             self.driver.close()





