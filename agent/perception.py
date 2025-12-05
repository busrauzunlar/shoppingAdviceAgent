from agent.scraper import scrape_trendyol

def get_user_request(category):
    print(f"{category} için ürün aranıyor...")
    return scrape_trendyol(category)
