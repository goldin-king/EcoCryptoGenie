from pycoingecko import CoinGeckoAPI
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import random

# nltk downloads (uncomment if running first time)
# nltk.download('punkt')
# nltk.download('stopwords')

cg = CoinGeckoAPI()

# Map your coins to CoinGecko IDs
coin_ids = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "Cardano": "cardano"
}

# Static sustainability scores and energy use (you can expand this)
sustainability_data = {
    "Bitcoin": {"energy_use": "high", "sustainability_score": 3/10},
    "Ethereum": {"energy_use": "medium", "sustainability_score": 6/10},
    "Cardano": {"energy_use": "low", "sustainability_score": 8/10}
}

greetings = ["Hey there!", "Yo! 👋", "Hi, future investor!", "Hello from EcoCryptoGenie! ✨"]
print(random.choice(greetings), "I'm EcoCryptoGenie — your friendly, green-minded crypto advisor!")
print("⚠️ Crypto is volatile. Always do your own research before investing!\n")

def clean_query(query):
    tokens = word_tokenize(query.lower())
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    return [word for word in tokens if word not in stop_words]

def get_real_time_data():
    # Fetch price and market data for all coins
    coin_list = list(coin_ids.values())
    data = cg.get_price(ids=coin_list, vs_currencies='usd', include_market_cap='true', include_24hr_change='true')
    return data

def respond_to_query(user_query):
    keywords = clean_query(user_query)

    data = get_real_time_data()

    # Real-time trending: look for coins with positive 24h price change
    trending_coins = [coin for coin, cg_id in coin_ids.items()
                      if data.get(cg_id) and data[cg_id].get('usd_24h_change', 0) > 0]

    # Sustainability
    if "sustainable" in keywords or "eco" in keywords or "green" in keywords:
        coin = max(sustainability_data, key=lambda x: sustainability_data[x]["sustainability_score"])
        score = sustainability_data[coin]["sustainability_score"]
        print(f"🌱 {coin} is the most eco-friendly choice with a sustainability score of {score:.1f}/1.0!")

    # Trending coins with real-time data
    elif "trend" in keywords or "rising" in keywords or "up" in keywords:
        if trending_coins:
            print(f"📈 Coins trending up in the last 24h: {', '.join(trending_coins)}")
        else:
            print("📉 No coins are trending up in the last 24 hours.")

    # Long-term growth suggestion (using price trend proxy)
    elif "long" in keywords or "growth" in keywords or "invest" in keywords:
        # Simple heuristic: coins with positive 24h change and high market cap (> $10B)
        candidates = []
        for coin, cg_id in coin_ids.items():
            coin_data = data.get(cg_id)
            if coin_data:
                market_cap = coin_data.get('usd_market_cap', 0)
                change_24h = coin_data.get('usd_24h_change', -100)
                if change_24h > 0 and market_cap > 10_000_000_000:
                    candidates.append((coin, market_cap))
        if candidates:
            best = max(candidates, key=lambda x: x[1])
            print(f"🚀 {best[0]} shows promising long-term growth potential based on current market cap and trends!")
        else:
            print("📉 No strong long-term candidates found based on current data.")

    # Energy use queries
    elif "energy" in keywords or "low" in keywords:
        low_energy = [coin for coin, data_ in sustainability_data.items() if data_["energy_use"] == "low"]
        if low_energy:
            print(f"🔋 Coins with low energy consumption: {', '.join(low_energy)}")
        else:
            print("⚡ Couldn't find low-energy coins right now.")

    # Help
    elif "help" in keywords:
        print("""
🧠 I can help you with:
- Most sustainable coins
- Trending cryptos based on last 24h price change
- Long-term investment options based on market cap
- Energy-efficient choices
- Just ask in simple English!
""")
    else:
        print("🤔 Sorry, I didn't catch that. Try asking about trends, sustainability, or long-term growth.")

# Chat loop
while True:
    user_query = input("💬 Ask EcoCryptoGenie (or type 'exit'): ")
    if user_query.lower() in ["exit", "quit"]:
        print("🧞‍♂️ Bye! May your coins be green and your growth exponential!")
        break
    respond_to_query(user_query)
