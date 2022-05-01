import json
import time

import numpy as np
from sdk import cache

start_timestamp = 1651323600


def uptake_documents():
    now = time.time()
    step = int((now - start_timestamp) / 100)

    types = ["common", "premium", "ultra"]

    all_buys = []

    for type in types:

        buys = json.loads(cache.get(f"{type}_buys"))

        for buy in buys:
            all_buys.append({
                "address": buy["address"],
                "qty": buy["qty"],
                "type": type
            })

    address_buys = {}

    for buy in all_buys:
        address = buy["address"]
        type = buy["type"]
        qty = buy["qty"]

        if (address not in address_buys.keys()):
            address_buys[address] = {
                "address": address,
                "common": 0,
                "premium": 0,
                "ultra": 0,
            }

        address_buys[address][type] += qty

    total_address = len(list(address_buys.keys()))
    avg_buys = {}

    for address_buy in address_buys.values():
        for type in types:
            if (type not in avg_buys.keys()):
                avg_buys[type] = {
                    "id": type,
                    "title": type.title(),
                    "updated": now,
                    "addresses": 0,
                    "total_addresses": total_address,
                    "qty": 0,
                    "avg": 0,
                    "uptake": 0
                }

            if (address_buy[type] > 0):
                avg_buys[type]["addresses"] += 1
                avg_buys[type]["qty"] += address_buy[type]
                avg_buys[type]["avg"] = avg_buys[type]["qty"] / avg_buys[type]["addresses"]
                avg_buys[type]["uptake"] = (avg_buys[type]["addresses"] / total_address) * 100
            


    return list(avg_buys.values())