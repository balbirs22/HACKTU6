from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---------------------------
# CONFIGURATION
# ---------------------------
LINKEDIN_EMAIL = "paveguardians@gmail.com"        # Your LinkedIn email
LINKEDIN_PASSWORD = "PaveGuardiansKhwaishJaiditya"  # Your LinkedIn password
ORGANIZATION_PEOPLE_URL = "https://www.linkedin.com/company/optum/people/"  # Target organization's people page URL
MESSAGE_TEXT = (
    "Hello, I came across your profile and would love to connect regarding opportunities at Optum. "
    "I'd appreciate any guidance or connections you could share. Thanks!"
)
NUM_RECIPIENTS = 3  # Number of profiles to send messages to

# ---------------------------
# SETUP WEBDRIVER AND OPTIONS
# ---------------------------
options = webdriver.ChromeOptions()
# For debugging, do not run headless so you can observe the browser actions.
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 30)

try:
    # ---------------------------
    # LOG IN TO LINKEDIN
    # ---------------------------
    driver.get("https://www.linkedin.com/login")
    username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_input = driver.find_element(By.ID, "password")
    
    username_input.send_keys(LINKEDIN_EMAIL)
    password_input.send_keys(LINKEDIN_PASSWORD)
    password_input.send_keys(Keys.RETURN)
    
    # Wait for a known post-login element (global search input) to confirm login succeeded
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.search-global-typeahead__input")))
    print("Login successful!")
    time.sleep(3)
    
    # ---------------------------
    # NAVIGATE TO ORGANIZATION'S PEOPLE PAGE
    # ---------------------------
    driver.get(ORGANIZATION_PEOPLE_URL)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(3)
    
    # Scroll down a bit to ensure profiles load
    driver.execute_script("window.scrollTo(0, 600);")
    time.sleep(2)
    
    # ---------------------------
    # COLLECT PROFILE LINKS
    # ---------------------------
    profile_links = []
    results = driver.find_elements(By.XPATH, "//a[contains(@href, '/in/')]")
    for res in results:
        href = res.get_attribute("href")
        if href and "linkedin.com/in/" in href and href not in profile_links:
            profile_links.append(href)
        if len(profile_links) >= NUM_RECIPIENTS:
            break
    
    if not profile_links:
        print("No profile links found on the organization's people page.")
        driver.quit()
        exit()
    
    # ---------------------------
    # ITERATE OVER PROFILES AND SEND MESSAGE
    # ---------------------------
    for link in profile_links:
        print("Processing profile:", link)
        driver.get(link)
        # Wait for a profile element to ensure page load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.profile-rail-card")))
        time.sleep(3)
        
        try:
            # Locate the Message button. Use a selector that finds a button containing the text "Message"
            message_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Message')]]"))
            )
            message_button.click()
            time.sleep(2)
            
            # Wait for the messaging dialog text area to appear.
            message_box = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.msg-form__contenteditable"))
            )
            message_box.click()  # Activate the text area
            time.sleep(1)
            
            # Type the cold message
            message_box.send_keys(MESSAGE_TEXT)
            time.sleep(1)
            
            # Wait until the send button is enabled (i.e., does not have the 'disabled' attribute)
            send_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.msg-form__send-button:not([disabled])"))
            )
            send_button.click()
            print("Message sent successfully to", link)
        except Exception as e:
            print("Failed to send message to", link, "due to", e)
        
        time.sleep(3)
    
except Exception as main_e:
    print("An error occurred during execution:", main_e)
    
finally:
    driver.quit()
