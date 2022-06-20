#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                            Cookie Clicker Game                                # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info: Uses Selenium automation to play Cookie Clicker game.                           #
#                                                                                       #
# Chromedriver Setup:                                                                   #
# Verify chromedriver path below: C:/path/to/chromedriver.exe                           #
# if not get latest stable Chromedriver: https://sites.google.com/chromium.org/driver   #
# Update Chrome Browser to latest: chrome://settings/help                               #
# On Windows add chromedriver path to Environmental Variables/System Variables          #
#                                                                                       #
# Launch Instructions:                                                                  #
# Rename project folder to your preference: cookie_clicker                              #
# Change path to project folder: cd cookie_clicker                                      #
# Create virtual environment: virtualenv venv                                           #
# Activate virtual enviornment: venv\scripts\activate                                   #
#                                                                                       #
# Requirements:                                                                         #
# pip3 install -U selenium                                                              #
# pip3 install webdriver-manager                                                        #
#                                                                                       #
# Launch by clicking run button in top right in VSCode or: py -3 main.py                #
#########################################################################################

from selenium import webdriver
import time
# Windows path is backslash, in VSCode it is forward slash to work:
chrome_driver_path = "C:/path/to/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

# Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break
