# agent/scraper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_trendyol(query, max_products=10):
    """Trendyol'dan gerçek zamanlı ürün çeker"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://www.trendyol.com/sr?q={query}")
    time.sleep(10)
    
    products = driver.find_elements(By.CSS_SELECTOR, "[data-testid='product-card']")
    results = []
    for p in products[:max_products]:
        try:
            name = p.find_element(By.TAG_NAME, "a").get_attribute("title")
            price = p.find_element(By.CSS_SELECTOR, ".prc-box-dscntd").text
            url = p.find_element(By.TAG_NAME, "a").get_attribute("href")
            results.append({"name": name, "price": price, "url": url})
        except:
            continue
    driver.quit()
    return results