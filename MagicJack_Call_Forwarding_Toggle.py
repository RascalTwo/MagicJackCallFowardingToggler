import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

call_forwarding = False


phone_number = getpass.getpass("Phone Number: ")
password = getpass.getpass("Password: ")

try:
    print "Starting"
    
    chrome_options = Options()
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get("https://web03.magicjack.com/my/index.html")

    driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))

    driver.execute_script("arguments[0].setAttribute('type', 'password')", driver.find_element_by_id("inpUsr"))
    driver.find_element_by_id("inpUsr").send_keys(phone_number)
    driver.find_element_by_id("inpPsw").send_keys(password)
    driver.find_element_by_id("inpPsw").send_keys(Keys.RETURN)

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "membername")))
    except:
        pass

    driver.get("https://account.magicjack.com/account/acmg/mj/callForward.do")
    driver.execute_script("arguments[0].innerText = '555-555-5555'", driver.find_element_by_id("device_816212"))
    driver.execute_script("arguments[0].innerText = ''", driver.find_element_by_css_selector("[href='renameDevice.do']"))    
    driver.execute_script("arguments[0].setAttribute('type', 'password')", driver.find_element_by_id("callfwdNum_816212"))
    driver.execute_script("arguments[0].innerText = 'Hi, ...'", driver.find_element_by_id("membername"))

    button = driver.find_elements(By.XPATH, "//input[starts-with(@name, 'imgme')]")[0]
    time.sleep(2.5)
    button.click()
    time.sleep(2.5)

    call_forwarding = False if button.get_attribute("name") == "imgme" else True

    driver.quit()

    print "Updating Current State..."

    selfLines = open(__file__, "r").readlines()

    line = (line for line in selfLines if line.startswith("call_forwarding")).next()

    selfLines[selfLines.index(line)] = line.replace(line.split("=")[1].strip(), str(call_forwarding))

    open(__file__, "w").writelines(selfLines)

    print "Success! Call Forwarding Is Now", "Off!" if call_forwarding == False else "On!"

except Exception, e:
    print "Something went wrong..."
    print e
    raise e
