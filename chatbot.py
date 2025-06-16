
# CryptoBuddy Chatbot

crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

BOT_NAME = "CryptoBuddy"

def bot_speak(message):
    print(f"{BOT_NAME}: {message}")

def handle_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        bot_speak(f"Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        bot_speak(f"These cryptos are trending up: {', '.join(trending)} 📈")

    elif "long-term" in user_query or "growth" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 0.7:
                bot_speak(f"{coin} is trending up and has a top-tier sustainability score! 🚀")
                return
        bot_speak("You might want to consider a balanced portfolio! 📊")

    else:
        bot_speak("Sorry, I’m still learning! Try asking about trending or sustainable coins. 🤖")

def chat():
    bot_speak("Hey there! I’m CryptoBuddy 🤖. Ask me about sustainable or trending cryptos!")
    bot_speak("⚠️ Crypto is risky—always do your own research before investing!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            bot_speak("Stay savvy and invest wisely! ✌️")
            break
        handle_query(user_input)

if __name__ == "__main__":
    chat()
