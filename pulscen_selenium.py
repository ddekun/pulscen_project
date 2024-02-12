from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

s = Service('./chromedriver')
options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=s, options=options)
# driver.implicitly_wait(10)
time.sleep(2)

list_companies = []
for page in range(1, 5):
    # time.sleep(1)
    url = f'https://noyabrsk.pulscen.ru/firms/070401-kabel-silovoj?page={page}'
    driver.get(url)

    # while True:
    #     try:
    #         button = driver.find_element(By.XPATH, "//span[contains(@class, 'ccdc-row ccd-phone-link js-show-phone-number js-ykr-action js-create-appeal-order')]")
    #         button.click()
    #         driver.implicitly_wait(10)
    #     except:
    #         break

    button = driver.find_elements(By.XPATH, "//span[contains(@class, 'ccdc-row ccd-phone-link js-show-phone-number js-ykr-action js-create-appeal-order')]")
    # time.sleep(1)
    try:
        for i in button:
            i.click()
            time.sleep(1)
            driver.implicitly_wait(10)

    except:
        # time.sleep(1)
        continue


    companies = driver.find_elements(By.XPATH, '//div[@class="ccd-content"]')
    # time.sleep(1)
    for company in companies:
        # companies_info = {}
        name = company.find_element(By.XPATH, './/a[@class="ccd-title js-bp-title js-ykr-action js-ga-link"]').text
        link = company.find_element(By.XPATH, './/a[@class="ccd-title js-bp-title js-ykr-action js-ga-link"]').get_attribute('href')
        address = company.find_element(By.XPATH, './/div[@class="ccda-row"]').text
        try:
            phone = company.find_element(By.XPATH, './/span[@class="ccdc-row ccd-phone-link js-show-phone-number js-ykr-action"]').text
        except:
            # time.sleep(1)
            phone = "Нет номера"

        companies_info = {'name': name, 'link': link, 'address': address, 'phone': phone}
        list_companies.append(companies_info)


pprint(list_companies)
print(len(list_companies))
df = pd.DataFrame(list_companies)
# df.to_csv("hanty_pulscen.csv")
writer = pd.ExcelWriter('noyabrsk_pulscen.xlsx')
df.to_excel(writer)
writer.save()

print()

# driver.close()
