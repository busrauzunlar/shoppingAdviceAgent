# agent/scoring.py - BÜTÇEYE GÖRE ÖNERİ
def suggest_products(products, budget):
    scored = []
    for p in products:
        if p['price'] == 'Fiyat yok':
            continue
        price_str = p['price'].replace(' TL', '').replace('.', '').replace(',', '')
        price = int(price_str) if price_str.isdigit() else 999999
        if price > budget:
            continue
        score = 0
        name_lower = p['name'].lower()
        if '16gb' in name_lower or '32gb' in name_lower:
            score += 2
        if '512gb' in name_lower or '1tb' in name_lower:
            score += 2
        if 'i7' in name_lower or 'ryzen 7' in name_lower:
            score += 3
        if 'rtx' in name_lower:
            score += 3
        score += 10 - (price // 1000)  # Fiyat düşükse +puan
        scored.append((p, score, price))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:3]