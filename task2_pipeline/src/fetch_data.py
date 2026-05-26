import requests
import logging

logging.basicConfig(level=logging.INFO)

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1
}

def fetch_crypto_data():
    try:
        logging.info("Fetching data from CoinGecko API...")

        response = requests.get(API_URL, params=params)

        response.raise_for_status()

        data = response.json()

        logging.info(f"Successfully fetched {len(data)} records")

        return data

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return []
