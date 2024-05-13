import os
import pickle


class UseCookies:
    def __init__(self, driver):
        self.driver = driver
        self.cookies = None
        self.file_name = "cookies.pkl"

    def write_cookies_to_file(self) -> None:
        """Write cookies to a file"""
        cookies = self.driver.get_cookies()
        file_path = os.path.join(os.getcwd(), self.file_name)
        with open(file_path, "wb") as file:
            pickle.dump(cookies, file)

    def load_cookies_from_file(self) -> None:
        """Load cookies from a file and add them to the current session"""
        file_path = os.path.join(os.getcwd(), self.file_name)
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                self.cookies = pickle.load(file)
            for cookie in self.cookies:
                self.driver.add_cookie(cookie)

    def delete_cookies(self) -> None:
        """Delete all cookies from the current session"""
        self.driver.delete_all_cookies()
        self.cookies = None

    def delete_cookies_file(self) -> None:
        """Delete the cookies file"""
        file_path = os.path.join(os.getcwd(), self.file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
