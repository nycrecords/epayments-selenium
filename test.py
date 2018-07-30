from selenium import webdriver
import sys
import unittest
import loginPage
import filterOrders

class Test(unittest.TestCase):
    def test(self):
        self.driver = webdriver.Chrome('/Users/bzhuang/Downloads/chromedriver')
        self.driver.get("https://10.155.227.154/")

        login = loginPage.Login(self.driver)
        login.login(self.user_type)

        filterthis = filterOrders.filterResults(self.driver)
        # filterthis.filter_by_type(self.user_type)
        filterthis.filter_by_status(self.user_type)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        Test.user_type = sys.argv.pop()
    unittest.main()
