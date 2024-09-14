# pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Page_object_model.base_page import BasePage

class MainPage(BasePage):
    # Locators for elements on the main page after logging into OrangeHRM
    USER_NAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    ADMIN = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Admin']")
    PIM = (By.XPATH, "//span[normalize-space()='PIM']")
    LEAVE = (By.XPATH, "//span[normalize-space()='Leave']")
    TIME = (By.XPATH, "//span[normalize-space()='Time']")
    RECRUITMENT = (By.XPATH, "//span[normalize-space()='Recruitment']")
    MY_INFO = (By.XPATH, "//span[normalize-space()='My Info']")
    PERFORMANCE = (By.XPATH, "//span[normalize-space()='Performance']")
    DASHBOARD = (By.XPATH, "//span[normalize-space()='Dashboard']")
    DIRECTORY = (By.XPATH, "//span[normalize-space()='Directory']")
    MAINTENANCE = (By.XPATH, "//span[normalize-space()='Maintenance']")
    CLAIM = (By.XPATH, "//span[normalize-space()='Claim']")
    BUZZ = (By.XPATH, "//span[normalize-space()='Buzz']")

    def Login_Orange_HRM(self, username, password):
        """
        Logs in to OrangeHRM with the provided username and password.

        :param username: Username to enter
        :param password: Password to enter
        """
        self.enter_text(self.USER_NAME, username)  # Enter username into the username field
        self.enter_text(self.PASSWORD, password)  # Enter password into the password field
        self.click_element(self.LOGIN_BUTTON)  # Click the login button

    def validate_admin_menu(self):
        """
        Validates that the Admin menu is visible on the main page.
        """
        admin = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.ADMIN)
        )
        assert admin.is_displayed(), "Admin menu is not visible"
        print("Admin menu is visible")

    def validate_PIM_menu(self):
        """
        Validates that the PIM (Personnel Information Management) menu is visible on the main page.
        """
        PIM = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.PIM)
        )
        assert PIM.is_displayed(), "PIM menu is not visible"
        print("PIM menu is visible")

    def validate_Leave_menu(self):
        """
        Validates that the Leave menu is visible on the main page.
        """
        leave = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.LEAVE)
        )
        assert leave.is_displayed(), "Leave menu is not visible"
        print("Leave menu is visible")

    def validate_Recruitment_menu(self):
        """
        Validates that the Recruitment menu is visible on the main page.
        """
        Recruitment = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.RECRUITMENT)
        )
        assert Recruitment.is_displayed(), "Recruitment menu is not visible"
        print("Recruitment menu is visible")

    def validate_Myinfo_menu(self):
        """
        Validates that the My Info menu is visible on the main page.
        """
        Myinfo = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.MY_INFO)
        )
        assert Myinfo.is_displayed(), "My Info menu is not visible"
        print("My Info menu is visible")

    def validate_Performance_menu(self):
        """
        Validates that the Performance menu is visible on the main page.
        """
        Performance = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.PERFORMANCE)
        )
        assert Performance.is_displayed(), "Performance menu is not visible"
        print("Performance menu is visible")

    def validate_Dashboard_menu(self):
        """
        Validates that the Dashboard menu is visible on the main page.
        """
        Dashboard = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.DASHBOARD)
        )
        assert Dashboard.is_displayed(), "Dashboard menu is not visible"
        print("Dashboard menu is visible")

    def validate_Directory_menu(self):
        """
        Validates that the Directory menu is visible on the main page.
        """
        Directory = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.DIRECTORY)
        )
        assert Directory.is_displayed(), "Directory menu is not visible"
        print("Directory menu is visible")

    def validate_Maintenance_menu(self):
        """
        Validates that the Maintenance menu is visible on the main page.
        """
        Maintenance = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.MAINTENANCE)
        )
        assert Maintenance.is_displayed(), "Maintenance menu is not visible"
        print("Maintenance menu is visible")

    def validate_Buzz_menu(self):
        """
        Validates that the Buzz menu is visible on the main page.
        """
        Buzz = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.BUZZ)
        )
        assert Buzz.is_displayed(), "Buzz menu is not visible"
        print("Buzz menu is visible")
