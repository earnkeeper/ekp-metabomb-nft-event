import json
from datetime import datetime

import requests
from decouple import config

from sdk import cache

api_key = config('BSCSCAN_API_KEY')
start_block = 17394712

def get_buys(address):
    buys = []
    count = 0
    page = 1
    page_size = 10000

    while (True):
        url = f'https://api.bscscan.com/api?module=account&action=txlist&address={address}&startblock={start_block}&page={page}&offset={page_size}&sort=asc&apiKey={api_key}'
        response = requests.get(url)

        trans = response.json()["result"]

        if (len(trans) == 0):
            break

        for tran in trans:
            input = tran["input"]
            method_id = input[0:10]
            if (method_id == "0xa5ae03d4"):
                qty = int(input[10:len(input)], 16)
                count += qty
                day = datetime.fromtimestamp(int(tran["timeStamp"]))
                buys.append(
                    {
                        "timestamp": int(tran["timeStamp"]),
                        "count": count,
                        "qty": qty,
                        "address": tran["from"]
                    }
                )

        if (len(trans) < page_size):
            break

        page += 1

    return buys


cache.set("common_buys", get_buys('0x1f36bef063ee6fcefeca070159d51a3b36bc68d6'))
cache.set("premium_buys", get_buys('0x2076626437c3bb9273998a5e4f96438abe467f1c'))
cache.set("ultra_buys", get_buys('0x9341faed0b86208c64ae6f9d62031b1f8a203240'))



