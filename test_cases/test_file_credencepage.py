

from selenium import webdriver



class Test_case_credencepage:
    def test_001(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == 'Credence':
            driver.save_screenshot("C:\\PYTHON PRACTICE\\seleniumDAY7\\Screen\\--Screenshot1.png")
            driver.close()
            assert True

        else:
            print('you are at wrong site')
            assert False

    # pytest - v - s - -html = HTMLR / report.html - -alluredir = "C:\PYTHON PRACTICE\seleniumDAY7\ALLUREREPORT"

    def test_002(self):
        a=10
        b=20
        sum=a+b
        if sum == 30:
            print('sum of a and b:',sum)
            assert True

        else:
            assert False



