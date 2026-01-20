# MIT License
# Copyright (c) 2026 Gabriel Yan

# if u use or share this code, pls keep the original credits.
# this project is for learning and experimental purposes.
# im just a nerd trying to get better :D 



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


# for some reason this options bellow make the captcha passthrough DONT MAKE ANYTHING UNLESS YOU KNOW WHAT YOU'RE DOING
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)


driver = webdriver.Chrome(options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
)
driver.maximize_window()


# this is the sleep time works for me, i gonna improve this later
time.sleep(2)
language_button = driver.find_element(By.ID, "langSelect-PT-BR")
language_button.click()

# captcha time
time.sleep(10)


cookie = driver.find_element(By.ID, "bigCookie")
cookie_count_element = driver.find_element(By.ID, "cookies")




items = []
i = 0

while True:
    try:
        price_element = driver.find_element(By.ID, f"productPrice{i}")
        item_element = driver.find_element(By.ID, f"product{i}")

        items.append((price_element, item_element))
        i += 1
    except:
        break


# UPGRADES NOT WORKING
upgrades = []
i = 0

while True:
    try:
        upgrade_element = driver.find_element(By.ID, f"upgrade{i}")
        upgrades.append((i, upgrade_element))
        i += 1
    except:
        break



for i in range(5000):
    cookie.click()


    cookies = int(
    cookie_count_element.text.split(" ")[0].replace(",", "")
    )

    for upgrade_id, upgrade_element in upgrades:
        can_buy = driver.execute_script(
            f"""
            let up = Game.UpgradesById[{upgrade_id}];
            return up.unlocked && !up.bought && Game.cookies >= up.getPrice();
            """
        )

        if can_buy:
            upgrade_element.click()
            break  

    
    cookies = int(
        cookie_count_element.text.split(" ")[0].replace(",", "")
    )

    
    for price_element, item_element in (items):
        try:
            price = int(price_element.text.replace(",", ""))
        except ValueError:
            continue

        if cookies >= price:
            item_element.click()
            break

 

time.sleep(600)