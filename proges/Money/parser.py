import requests

import config

headers = {"User-Agent": config.USER, "Accept": "text/html", "Apikey": config.API_KEY}


def get_currency(from_cur, to_cur):
    data = requests.get(config.URL, headers=headers).json()["data"]
    dollar_val = data[from_cur.upper()]['value']
    if (to_cur := to_cur.upper()) != "USD":
        dollar_val = data[to_cur]['value'] / dollar_val
    return dollar_val
