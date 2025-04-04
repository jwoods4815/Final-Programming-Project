import csv
import random
from datetime import datetime, timedelta

categories = {
    "Bills": ["Con Edison Electric", "Verizon Wireless", "Spectrum Internet", "State Farm Insurance", "Geico Auto Insurance"],
    "Online Stores": ["Amazon", "eBay", "Walmart.com", "Best Buy", "Etsy"],
    "Subscriptions": ["Netflix", "Spotify", "Disney+", "Amazon Prime", "Apple Music"],
    "Groceries": ["Whole Foods", "Trader Joe's", "Kroger", "Costco", "Aldi"],
    "Dining Out": ["McDonald's", "Starbucks", "Chipotle", "Olive Garden", "Shake Shack"]
}

def random_amount(category):
    if category == "Bills": return round(random.uniform(50, 200), 2)
    elif category == "Groceries": return round(random.uniform(40, 120), 2)
    elif category == "Dining Out": return round(random.uniform(5, 45), 2)
    elif category == "Subscriptions": return random.choice([9.99, 12.99, 14.99, 19.99])
    else: return round(random.uniform(10, 250), 2)

start_date = datetime(2023, 7, 1)
with open('transactions_500.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['date','amount','category','description'])
    
    for i in range(500):
        category = random.choice(list(categories.keys()))
        date = (start_date + timedelta(days=i//2)).strftime('%Y-%m-%d')
        writer.writerow([
            date,
            random_amount(category),
            category,
            random.choice(categories[category])
        ])