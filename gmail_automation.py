from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function to create a Gmail account
def create_gmail_account(first_name, last_name, username, birthday, gender, password):
    try:
        # Initialize Chrome WebDriver with options
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-infobars")  # Disable info bars
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options = option)
        wait = WebDriverWait(driver, timeout=10)

        # Navigate to the Gmail sign up page
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

        # Fill in first name and last name
        first_name_field = driver.find_element(By.NAME, "firstName")
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = driver.find_element(By.NAME, "lastName")
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        time.sleep(3)
        # Click on the next button
        next_button = driver.find_element(By.XPATH, "//span[text()='Sljedeće']")
        next_button.click()

        # Wait for the birthday fields to appear
        wait.until(EC.visibility_of_element_located((By.NAME, "day")))

        # Split birthday into day, month, and year
        birthday_elements = birthday.split()

        # Select birthday from dropdowns
        month_dropdown = Select(driver.find_element(By.ID, "month"))
        month_dropdown.select_by_value(birthday_elements[1])

        day_field = driver.find_element(By.ID, "day")
        day_field.clear()
        day_field.send_keys(birthday_elements[0])

        year_field = driver.find_element(By.ID, "year")
        year_field.clear()
        year_field.send_keys(birthday_elements[2])

        # Select gender from dropdown
        gender_dropdown = Select(driver.find_element(By.ID, "gender"))
        gender_dropdown.select_by_value(gender)

        # Click on the next button
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        # Select option to create own email
        create_own_option = wait.until(EC.element_to_be_clickable((By.ID, "selectionc2")))
        create_own_option.click()

        # Fill in username
        username_field = driver.find_element(By.NAME, "Username")
        username_field.clear()
        username_field.send_keys(username)

        # Click on the next button
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        # Fill in password
        password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
        password_field.clear()
        password_field.send_keys(password)

        # Confirm password
        password_confirmation_field = driver.find_element(By.NAME, "PasswdAgain")
        password_confirmation_field.clear()
        password_confirmation_field.send_keys(password)

        # Click on the next button
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        # Skip adding phone number
        skip_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        skip_button.click()

        # Skip adding recovery email
        skip_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        skip_button.click()

        # Click on the next button
        next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe")))
        next_button.click()

        # Agree on Google's privacy
        agree_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        agree_button.click()

        print("Your Gmail account has been successfully created:\n")
        print("Username: " + username + "@gmail.com")
        print("Password: " + password)

    except (NoSuchElementException, TimeoutException) as e:
        print("Failed to create your Gmail account. Error: " + str(e))

    finally:
        driver.quit()

# Example usage
if __name__ == "__main__":
    create_gmail_account("Lamija", "Mezit", "l.mezit26", "07 26 1999", "2", "x,nscldsj123...FDKZ")