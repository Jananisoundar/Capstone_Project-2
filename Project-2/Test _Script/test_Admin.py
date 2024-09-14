# tests/test_login.py

import pytest
from Page_object_model.Admin_page import AdminPage

@pytest.mark.usefixtures("setup")
class TestAdminMenus:
    """
    Test class for validating admin menus after logging into OrangeHRM.
    """

    def test_login_and_validate_adminmenus(self):
        """
        Test case for logging into OrangeHRM and validating the visibility of various admin menus.
        """
        admin_page = AdminPage(self.driver)  # Create an instance of AdminPage with the WebDriver

        # Step 1: Perform login
        admin_page.Login_Orange_HRM("Admin", "admin123")  # Log in with provided username and password

        # Step 2: Validate successful login by checking the page title
        assert self.driver.title == "OrangeHRM", f"Expected title to be 'OrangeHRM', but got '{self.driver.title}'"
        print(self.driver.title)  # Print the page title
        print("Assertion passed")  # Indicate that the title assertion passed

        # Step 3: Click on the Admin menu
        admin_page.click_on_Admin_menu()

        # Step 4: Optionally click on the collapse icon if needed (for navigation)
        admin_page.Click_on_collpase()

        # Step 5: Validate the visibility of various admin menus
        admin_page.validate_user_management_menu()  # Validate User Management menu
        admin_page.validate_job_menu()  # Validate Job menu
        admin_page.validate_Organization_menu()  # Validate Organization menu
        admin_page.validate_Qualification_menu()  # Validate Qualification menu
        admin_page.validate_Nationalities_menu()  # Validate Nationalities menu
        admin_page.validate_Corporatebranding_menu()  # Validate Corporate Branding menu
        admin_page.validate_Configuration_menu()  # Validate Configuration menu
