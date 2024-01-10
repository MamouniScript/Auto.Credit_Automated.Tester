import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Replace these values with the actual information
url = ""
username = ""
password = ""

# Specify the path to the downloaded Microsoft Edge WebDriver executable
edgedriver_path = r""

# Set up the EdgeOptions
edge_options = webdriver.EdgeOptions()
edge_options.binary_location = r""  # Update this path

# Set up the EdgeService
service = webdriver.EdgeService(executable_path=edgedriver_path)

# Set up the Edge WebDriver with options and service
driver = webdriver.Edge(service=service, options=edge_options)

try:
    # Maximize the window
    driver.maximize_window()

    # Navigate to the URL
    driver.get(url)





                            
#***************************************** Wait for the "Accès Crédit Auto" button to be present ************************************************************************************


    access_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Accès Crédit Auto")))
    access_button.click()



    # Locate the login elements without handling TimeoutException
    username_field = driver.find_element(By.NAME, "_username")
    password_field = driver.find_element(By.NAME, "_password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")




    # Enter the username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click the login button
    login_button.click()




     # Find the third "Cliquez ici" link by its link text and click
    simulation_button = driver.find_elements(By.LINK_TEXT, "Cliquez ici")[2]
    simulation_button.click()

    print("Login successful!")




    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")




    # Filling the form correctly
    driver.find_element(By.ID, "form_simulation_montantAchat").send_keys("10000")
    driver.find_element(By.ID, "form_simulation_montantCredit").send_keys("8000")
    driver.find_element(By.ID, "form_simulation_duree").send_keys("24")

    # Selecting a valid Categorie value ('A' or 'B')
    categorie_select = Select(driver.find_element(By.ID, "form_simulation_categorie"))
    categorie_select.select_by_value("A")  # or "B"

    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    # Printing a success message
    print("Form filled correctly.")

    # Submit the form
    driver.find_element(By.ID, "calcul").click()

    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    # Print the custom success notification
    print("Simulation done with correct values")



# *****************                   test anther scenario with incorrect inpputs                   ****************************
    # # Refresh the page
    # driver.refresh()



    # # Filling the form incorrectly
    # driver.find_element(By.ID, "form_simulation_montantAchat").send_keys("3000")  # Below the minimum value
    # driver.find_element(By.ID, "form_simulation_montantCredit").send_keys("5000")  # Below the required 80% of Montant Achat
    # driver.find_element(By.ID, "form_simulation_duree").send_keys("60")  # Above the maximum value

    # # Selecting an invalid Categorie value
    # categorie_select.select_by_value("A")

    # # Printing an error message
    # print("Form filled incorrectly.")

    # # Submit the form
    # driver.find_element(By.ID, "calcul").click()


    # # Print the custom error notification
    # print("Simulation failed with incorrect values")


# *****************                   test anther scenario with incorrect inpputs                   ****************************


    # Wait to read cout credit
    time.sleep(7)

    # Scroll to the top of the page
    driver.execute_script("window.scrollTo(0, 0);")


    # Logout
    driver.find_element(By.ID, "lnkDeconnexion").click()
    print("Déconnecté")


except (TimeoutException, NoSuchElementException) as e:
    print(f"Exception: {e}")

finally:
    # Add a delay of, for example, 5 seconds before quitting the driver
    time.sleep(5)
    
    # Close the browser window
    driver.quit()