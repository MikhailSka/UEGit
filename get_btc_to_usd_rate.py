import requests

def get_btc_to_usd_rate():

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd"}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        btc_to_usd_rate = data["bitcoin"]["usd"]
        return btc_to_usd_rate
    else:
        # Handle the error case, e.g., return a default value or raise an exception
        return None
