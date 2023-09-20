from datetime import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    '''Method to print current URL'''

    def print_current_url(self):
        current_url = self.driver.current_url
        print(f"Current url: {current_url}")

    '''Method assert a word'''

    def assert_word(self, word, exp_word):
        value_word = word.text
        assert value_word == exp_word
        print("The values are the same")

    '''Method to make a screenshot'''

    def make_screenshot(self):
        now_date = datetime.now().strftime("%Y.%m.%d %H.%M.%S")
        name_screenshot = f"screen_{now_date}.png"
        self.driver.save_screenshot(f"screen/{name_screenshot}")

    '''Method to assert a url'''
    def assert_url(self, exp_res):
        current_url = self.driver.current_url
        assert current_url == exp_res
        print("URLs are the same")