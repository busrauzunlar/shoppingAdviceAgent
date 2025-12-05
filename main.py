from agent.scoring import suggest_products

# ... (scrape_trendyol sonrası)
budget = int(input("Bütçen ne kadar? (TL): "))
suggestions = suggest_products(products, budget)
for i, (p, score, price) in enumerate(suggestions, 1):
    print(f"{i}. Öneri: {p['name']} (Skor: {score}, Fiyat: {price} TL)")