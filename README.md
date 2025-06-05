# EcoCryptoGenie
crypto chat bot
# EcoCryptoGenie

EcoCryptoGenie is a simple yet powerful Python chatbot that helps users make eco-friendly and informed cryptocurrency investment decisions. It combines real-time crypto market data from the CoinGecko API with sustainability metrics to recommend coins based on trends, energy use, and long-term growth potential.

---

## Features

- **Real-time crypto data:** Fetches up-to-date prices, 24-hour price changes, and market capitalization using CoinGecko’s free API.
- **Sustainability scores:** Static scores indicating energy consumption and environmental friendliness.
- **Natural language understanding:** Basic keyword-based NLP using NLTK to understand user queries.
- **Advice categories:** Users can ask about trending coins, sustainable options, long-term investments, or energy-efficient cryptos.
- **Friendly and engaging personality:** Provides responses in a casual, easy-to-understand tone.
- **Disclaimer:** Reminds users about the risks involved in crypto investing.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/goldin-king/EcoCryptoGenie.git
   cd EcoCryptoGenie
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
Install the required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not present, install manually:

bash
Copy
Edit
pip install pycoingecko nltk
Download NLTK data (only needed once):

python
Copy
Edit
import nltk
nltk.download('punkt')
nltk.download('stopwords')
Usage
Run the chatbot script:

bash
Copy
Edit
python eco_crypto_genie.py
Interact with the chatbot by typing queries such as:

"Which crypto is trending up?"

"What’s the most sustainable coin?"

"Which coin should I invest in for long-term growth?"

"Tell me about energy-efficient cryptocurrencies."

Type exit or quit to end the session.

Project Structure
bash
Copy
Edit
EcoCryptoGenie/
├── eco_crypto_genie.py      # Main chatbot Python script
├── README.md                # This file
├── requirements.txt         # Python dependencies (optional)
└── screenshots/             # Optional: Screenshots of chatbot interactions
How does this chatbot mimic basic AI decision-making?
EcoCryptoGenie uses a combination of real-time data retrieval and simple natural language processing to interpret user queries. It applies conditional logic to match keywords with cryptocurrency attributes like price trends and sustainability scores, thereby simulating decision-making to provide personalized, informative responses.

Disclaimer
Cryptocurrency investing is volatile and risky. This chatbot is for educational purposes only and does not constitute financial advice. Always conduct your own research before making investment decisions.

Contribution
Feel free to fork this project and add more features such as:

Support for more cryptocurrencies

Advanced NLP with machine learning

GUI/web interface

Integration with other APIs

Contact
Created by [Ray Onyango]
Email: rayopiyo1@gmail.com
GitHub: https://github.com/goldin-king
