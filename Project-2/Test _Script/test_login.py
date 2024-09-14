# tests/test_login.py

import pytest
from Page_object_model.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    """
    Test class for login functionalities including the 'Forgot Password' feature.
    """

    def test_forgot_password(self):
        """
        Test case for verifying the 'Forgot Password' functionality.
        """
        login_page = LoginPage(self.driver)  # Create an instance of LoginPage with the WebDriver

        # Step 1: Click on the "Forgot your password?" link to initiate the password reset process
        login_page.Click_on_Forgot_password_link()

        # Step 2: Enter the username associated with the account for which the password needs to be reset
        login_page.Enter_username("Admin")

        # Step 3: Click on the "Reset Password" button to submit the password reset request
        login_page.Click_on_Forgot_password()

        # Step 4: Validate that a message confirming the password reset request is displayed
        login_page.validate_message()  # Ensure that the confirmation message or redirection is correct

        # Optional Step: Validate redirection or success message if applicable
        # This step depends on how the application responds after a reset request (e.g., redirect to a confirmation page)
