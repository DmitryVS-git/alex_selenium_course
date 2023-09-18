class Base:

    def __init__(self, driver):
        self.driver = driver

    '''Method to get current URL'''
    def print_current_url(self):
        current_url = self.driver.current_url
        print(f"Current url: {current_url}")