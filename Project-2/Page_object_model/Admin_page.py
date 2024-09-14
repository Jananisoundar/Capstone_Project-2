# pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Page_object_model.base_page import BasePage

class AdminPage(BasePage):
    # Locators for various elements on the admin page
    USER_NAME = (By.XPATH,"//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH,"//button[normalize-space()='Login']")
    ADMIN_MENU = (By.XPATH, "//span[normalize-space()='Admin']")
    COLLPASE = (By.XPATH,"//i[@class='oxd-icon bi-chevron-left']")
    USER_MANAGEMENT = (By.XPATH, "(//span[normalize-space()='User Management'])[1]")
    JOB = (By.XPATH, "(//span[normalize-space()='Job'])[1]")
    ORGANIZATION = (By.XPATH, "//span[normalize-space()='Organization']")
    QUALIFICATION = (By.XPATH,"//span[normalize-space()='Qualifications']")
    NATIONALITIES = (By.XPATH, "//a[normalize-space()='Nationalities']")
    CORPORATE_BANKING = (By.XPATH, "//a[normalize-space()='Corporate Branding']")
    CONFIGURATION = (By.XPATH, "(//a[normalize-space() = 'Configuration'])[1]")

    def Login_Orange_HRM(self, username, password):
        """
        Logs in to the Orange HRM application using the provided username and password.

        :param username: Username to enter
        :param password: Password to enter
        """
        self.enter_text(self.USER_NAME, username)  # Enter username into the username field
        self.enter_text(self.PASSWORD, password)  # Enter password into the password field
        self.click_element(self.LOGIN_BUTTON)  # Click the login button

    def click_on_Admin_menu(self):
        """
        Clicks on the Admin menu.
        """
        self.click_element(self.ADMIN_MENU)  # Click the Admin menu item

    def Click_on_collpase(self):
        """
        Clicks on the collapse icon to hide or show menu items.
        """
        self.click_element(self.COLLPASE)  # Click the collapse icon

    def validate_user_management_menu(self):
        """
        Validates that the User Management menu is visible on the page.
        """
        user_management = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.USER_MANAGEMENT)
        )
        assert user_management.is_displayed(), "User Management menu is not visible"
        print("User Management menu is visible")

    def validate_job_menu(self):
        """
        Validates that the Job menu is visible on the page.
        """
        job = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.JOB)
        )
        assert job.is_displayed(), "Job menu is not visible"
        print("Job menu is visible")

    def validate_Organization_menu(self):
        """
        Validates that the Organization menu is visible on the page.
        """
        Organization = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.ORGANIZATION)
        )
        assert Organization.is_displayed(), "Organization menu is not visible"
        print("Organization menu is visible")

    def validate_Qualification_menu(self):
        """
        Validates that the Qualification menu is visible on the page.
        """
        Qualification = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.QUALIFICATION)
        )
        assert Qualification.is_displayed(), "Qualification menu is not visible"
        print("Qualification menu is visible")

    def validate_Nationalities_menu(self):
        """
        Validates that the Nationalities menu is visible on the page.
        """
        Nationalities = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.NATIONALITIES)
        )
        assert Nationalities.is_displayed(), "Nationalities menu is not visible"
        print("Nationalities menu is visible")

    def validate_Corporatebranding_menu(self):
        """
        Validates that the Corporate Branding menu is visible on the page.
        """
        Corporatebranding = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.CORPORATE_BANKING)
        )
        assert Corporatebranding.is_displayed(), "Corporate Branding menu is not visible"
        print("Corporate Branding menu is visible")

    def validate_Configuration_menu(self):
        """
        Validates that the Configuration menu is visible on the page.
        """
        Configuration = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.CONFIGURATION)
        )
        assert Configuration.is_displayed(), "Configuration menu is not visible"
        print("Configuration menu is visible")
