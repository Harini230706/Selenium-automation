from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

import os
import time


chrome_options = Options()

driver = webdriver.Chrome(options=chrome_options)


try:

    file_path="file:///"+os.path.abspath("calculator.html")

    driver.get(file_path)

    print("Page Title:",driver.title)


    # Addition Test

    driver.find_element(By.ID,"num1").clear()

    driver.find_element(By.ID,"num1").send_keys("10")

    driver.find_element(By.ID,"num2").clear()

    driver.find_element(By.ID,"num2").send_keys("5")

    driver.find_element(By.ID,"addBtn").click()

    time.sleep(1)

    result=driver.find_element(By.ID,"result").text

    print("Addition Result:",result)

    assert "15" in result

    print("Addition Test PASSED")


    # Subtraction Test

    driver.find_element(By.ID,"num1").clear()

    driver.find_element(By.ID,"num1").send_keys("10")

    driver.find_element(By.ID,"num2").clear()

    driver.find_element(By.ID,"num2").send_keys("4")

    driver.find_element(By.ID,"subBtn").click()

    time.sleep(1)

    result=driver.find_element(By.ID,"result").text

    print("Subtraction Result:",result)

    assert "6" in result

    print("Subtraction Test PASSED")


finally:

    driver.quit()

    print("All tests completed")