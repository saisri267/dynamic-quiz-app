import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ==================================================
# CONFIG
# ==================================================
LANDING_URL = "http://localhost/Dynamic_PHP_Quiz_App/index.php"
QUIZ_URL = "http://localhost/Dynamic_PHP_Quiz_App/quiz.php?category=web&difficulty=easy"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def screenshot(name):
    path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(path)
    print("📸 Screenshot:", path)

# ==================================================
# DRIVER SETUP
# ==================================================
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
    # ==================================================
    # TC1 – Landing Page (Category & Difficulty)
    # ==================================================
    print("\nTC1: Landing Page – Category & Level")

    driver.get(LANDING_URL)

    # ✅ WAIT FOR FULL PAGE LOAD (JS + CSS)
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    # ✅ WAIT FOR ANY REAL LANDING UI ELEMENT
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "select, button, .card, .container")
        )
    )

    time.sleep(1)  # allow gradient + animation to settle

    print("URL:", driver.current_url)
    print("Title:", driver.title)

    screenshot("TC1_Landing_Page")


    # ==================================================
    # TC2 – First Question Loaded
    # ==================================================
    print("\nTC2: First Question Loaded")

    # Navigate explicitly to quiz page
    driver.get(QUIZ_URL)

    # 🔥 WAIT UNTIL QUESTION TEXT IS ACTUALLY LOADED
    wait.until(
        lambda d: len(d.find_element(By.ID, "question").text.strip()) > 0
    )

    question = driver.find_element(By.ID, "question")
    print("Question:", question.text)

    screenshot("TC2_First_Question")

    # ==================================================
    # TC3 – Negative: Next without selecting option
    # ==================================================
    print("\nTC3: Negative – Next without selection")

    driver.find_element(By.ID, "nextBtn").click()

    warning = wait.until(
        EC.visibility_of_element_located((By.ID, "warning"))
    )
    print("Warning:", warning.text)

    screenshot("TC3_Negative_Select_Option")

    # ==================================================
    # TC4 – Select option AFTER warning appears
    # ==================================================
    print("\nTC4: Select option after warning")

    options = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[name='ans']"))
    )
    options[0].click()

    screenshot("TC4_Select_After_Warning")

    driver.find_element(By.ID, "nextBtn").click()

    # ==================================================
    # TC5 – Answer remaining questions randomly (ONE screenshot)
    # ==================================================
    print("\nTC5: Random Answering")

    tc5_screenshot_taken = False

    while True:
        time.sleep(0.4)

        options = driver.find_elements(By.CSS_SELECTOR, "input[name='ans']")
        if options:
            random.choice(options).click()

            if not tc5_screenshot_taken:
                screenshot("TC5_Random_Answering")
                tc5_screenshot_taken = True

            driver.find_element(By.ID, "nextBtn").click()
        else:
            break

        if driver.find_elements(By.CLASS_NAME, "result"):
            break

    # ==================================================
    # TC6 – Result & Score Page
    # ==================================================
    print("\nTC6: Result Page")

    result_box = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "result"))
    )

    result_text = result_box.text
    print(result_text)

    assert "Score" in result_text
    assert "Quiz Completed" in result_text

    screenshot("TC6_Result_Page")

    print("\n✅ ALL 6 TEST CASES PASSED SUCCESSFULLY")

finally:
    time.sleep(2)
    driver.quit()
