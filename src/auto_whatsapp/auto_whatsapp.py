#####== SELENIUM BASED WHATSAPP BOT ==#####
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

WINDOWS_USERNAME = "ADIL"

# Group msg
def sendChat(numbers, msg):
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir=C:\\Users\\{{WINDOWS_USERNAME}}\\AppData\\Local\\Google\\Chrome\\UserData")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://web.whatsapp.com/')
    wait = WebDriverWait(driver, 300)

    for i in range(len(numbers)):
        user_arg = '//span[@title=' + '"' + numbers[i] + '"' + '][@dir="auto"]'
        user = wait.until(EC.presence_of_element_located((By.XPATH, user_arg)))
        user.click()
        sleep(4)

        msg_box_arg = '//div[@class="p3_M1"]'
        msg_box = wait.until(EC.presence_of_element_located((By.XPATH, msg_box_arg)))
        msg_box.send_keys(msg + Keys.RETURN)
        sleep(3)

    sleep(3)
    print('Messages send successfully')
    driver.quit()


# Send document
def sendDoc(numbers, path):
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir=C:\\Users\\{{WINDOWS_USERNAME}}\\AppData\\Local\\Google\\Chrome\\UserData")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://web.whatsapp.com/')
    wait = WebDriverWait(driver, 300)

    for i in range(len(numbers)):
        user_arg = '//span[@title="' + numbers[i] + '"][@dir="auto"]'
        user = wait.until(EC.presence_of_element_located((By.XPATH, user_arg)))
        user.click()
        sleep(3)

        attach_arg = '//span[@data-testid="clip"]'
        attach = wait.until(EC.presence_of_element_located((By.XPATH, attach_arg)))
        attach.click()
        sleep(2)

        doc_box_arg = '//input[@accept="*"][@type="file"]'
        doc_box = wait.until(EC.presence_of_element_located((By.XPATH, doc_box_arg)))
        doc_box.send_keys(path)
        sleep(3)

        send_arg = '//span[@data-testid="send"]'
        send = wait.until(EC.presence_of_element_located((By.XPATH, send_arg)))
        send.click()
        sleep(3)

    sleep(5)
    driver.quit()


# Send media
def sendMedia(numbers, path):
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir=C:\\Users\\{{WINDOWS_USERNAME}}\\AppData\\Local\\Google\\Chrome\\UserData")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://web.whatsapp.com/')
    wait = WebDriverWait(driver, 300)


    for i in range(len(numbers)):
        user_arg = '//span[@title="' + numbers[i] + '"][@dir="auto"]'
        user = wait.until(EC.presence_of_element_located((By.XPATH, user_arg)))
        user.click()
        sleep(3)

        attach_arg = '//span[@data-testid="clip"]'
        attach = wait.until(EC.presence_of_element_located((By.XPATH, attach_arg)))
        attach.click()
        sleep(2)

        doc_box_arg = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"][@type="file"]'
        doc_box = wait.until(EC.presence_of_element_located((By.XPATH, doc_box_arg)))
        doc_box.send_keys(path)
        sleep(5)

        send_arg = '//span[@data-testid="send"]'
        send = wait.until(EC.presence_of_element_located((By.XPATH, send_arg)))
        send.click()
        sleep(3)

    sleep(5)
    driver.quit()
