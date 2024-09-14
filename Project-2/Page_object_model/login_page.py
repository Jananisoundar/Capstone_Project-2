# pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Page_object_model.base_page import BasePage

class LoginPage(BasePage):
    # Locators for elements on the login page related to the forgot password functionality
    FORGOT_YOUR_PASSWORD = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
    USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    RESET_PASSWORD_BUTTON = (By.XPATH, "//button[normalize-space()='Reset Password']")
    MESSAGE = (By.XPATH, "(//h6[normalize-space()='Reset Password link sent successfully'])[1]")

    def Forgot_password_validation(self):
        """
        Ensures that the 'Forgot your password?' link is clickable before interacting with it.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FORGOT_YOUR_PASSWORD)
        )

    def Click_on_Forgot_password_link(self):
        """
        Clicks on the 'Forgot your password?' link to initiate the password reset process.
        """
        self.click_element(self.FORGOT_YOUR_PASSWORD)

    def Enter_username(self, username):
        """
        Enters the username into the username field for the password reset request.

        :param username: Username to be entered into the field
        """
        self.enter_text(self.USERNAME, username)

    def Click_on_Forgot_password(self):
        """
        Clicks on the 'Reset Password' button to submit the password reset request.
        """
        self.click_element(self.RESET_PASSWORD_BUTTON)

    def validate_message(self):
        """
        Validates that the confirmation message for the password reset request is displayed.

        This method waits for the message element to be visible and then checks that its text
        matches the expected message.
        """
        # Extend timeout and wait for the message to be visible
        message_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.MESSAGE)
        )
        actual_message = message_element.text
        expected_message = "Reset Password link sent successfully"

        # Validate the actual message
        assert actual_message == expected_message, f"Expected '{expected_message}', but got '{actual_message}'"
