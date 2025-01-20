from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def data_collect_service():
    chromedriver_path = r"C:\Users\User\Documents\GitHub\GitHubGabrielLima\Projetos-GabrielLima\Coletor-de-perifericos-Kabum\src\chromedriver.exe"

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--headless")

    bot = webdriver.Chrome(executable_path=chromedriver_path, options=options)

    try:
        print("Começando o processo de coletar dados dos periféricos da Kabum")
        bot.get("https://www.kabum.com.br/")
        
        list_items, list_peripherals = [], ["Teclado Gamer", "Mouse Gamer", "Headset Gamer","Monitor Gamer", "Cadeira Gamer"]
        
        while list_peripherals:
            search = bot.find_element(By.NAME, "query")
            search.send_keys(list_peripherals[0])
            search.send_keys(Keys.RETURN)
            for i in range(1,11):
                xpath_title= f'//*[@id="listing"]/div[3]/div/div/div[2]/div/main/div[{i}]/article/a/div/button/div/h3/span'
                xpath_link_image= f'//*[@id="listing"]/div[3]/div/div/div[2]/div/main/div[{i}]/article/a/img'
                xpath_old_price= f'//*[@id="listing"]/div[3]/div/div/div[2]/div/main/div[{i}]/article/a/div/div[2]/div[1]/span[1]'
                xpath_price= f'//*[@id="listing"]/div[3]/div/div/div[2]/div/main/div[{i}]/article/a/div/div[2]/div[2]/span'
                xpath_link_product= f'//a[@class="sc-27518a44-4 kVoakD productLink"]'
                
                time.sleep(1)
                
                title = bot.find_element(By.XPATH, xpath_title).text
                link_image = bot.find_element(By.XPATH, xpath_link_image).get_attribute("src")
                old_price = bot.find_element(By.XPATH, xpath_old_price).text
                price = bot.find_element(By.XPATH, xpath_price).text
                link_product = bot.find_element(By.XPATH, xpath_link_product).get_attribute("href")
                                
                list_items.append({
                    "classification": list_peripherals[0],
                    "title": title,
                    "link_image": link_image,
                    "old_price": old_price if old_price != "" else "Sem informações anteriores",
                    "price": price if old_price != "" else "Sem informações recentes",
                    "link_product": link_product,
                })
            
            list_peripherals.pop(0)
            time.sleep(2)
                
    finally:
        bot.quit()
        return list_items