# tests/test_main_menus.py

import pytest
from Page_object_model.Main_page import MainPage


@pytest.mark.usefixtures("setup")
class TestMainMenus:
    """
    Test class for validating main menu items after logging into OrangeHRM.
    """

    def test_login_and_validate_mainmenus(self):
        """
        Test case for logging into OrangeHRM and validating the visibility of various main menus.
        """
        main_page = MainPage(self.driver)  # Create an instance of MainPage with the WebDriver

        # Step 1: Perform login with provided username and password
        main_page.Login_Orange_HRM("Admin", "admin123")

        # Step 2: Validate that each main menu is visible on the page
        main_page.validate_admin_menu()  # Validate visibility of the Admin menu
        main_page.validate_PIM_menu()  # Validate visibility of the PIM (Personnel Information Management) menu
        main_page.validate_Leave_menu()  # Validate visibility of the Leave menu
        main_page.validate_Recruitment_menu()  # Validate visibility of the Recruitment menu
        main_page.validate_Myinfo_menu()  # Validate visibility of the My Info menu
        main_page.validate_Performance_menu()  # Validate visibility of the Performance menu
        main_page.validate_Dashboard_menu()  # Validate visibility of the Dashboard menu
        main_page.validate_Directory_menu()  # Validate visibility of the Directory menu
        main_page.validate_Maintenance_menu()  # Validate visibility of the Maintenance menu
        main_page.validate_Buzz_menu()  # Validate visibility of the Buzz menu
