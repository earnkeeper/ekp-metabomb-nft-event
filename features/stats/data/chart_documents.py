import json
import time

from sdk import cache

start_timestamp = 1651323600


def chart_documents():
    now = time.time()
    step = int((now - start_timestamp) / 100)

    common_buys = json.loads(cache.get("common_buys"))
    premium_buys = json.loads(cache.get("premium_buys"))
    ultra_buys = json.loads(cache.get("ultra_buys"))

    buys = {}

    process_buys(common_buys, "common", buys, step, now)
    process_buys(premium_buys, "premium", buys, step, now)
    process_buys(ultra_buys, "ultra", buys, step, now)

    cum_sold = {
        "common": 0,
        "premium": 0,
        "ultra": 0
    }

    def sort_fn(buy):
        return buy["timestamp"]

    sorted_buys = list(buys.values())
    sorted_buys.sort(key=sort_fn)

    accumulate_buys(sorted_buys, cum_sold)

    sorted_buys.insert(
        0,
        {
            "id": start_timestamp - step,
            "timestamp": start_timestamp - step,
            "timestamp_ms": (start_timestamp - step) * 1000,
            "updated": now,
            "common_sold": 0,
            "premium_sold": 0,
            "ultra_sold": 0,
            "cum_sold": 0,
            "cum_common_sold": 0,
            "cum_premium_sold": 0,
            "cum_ultra_sold": 0,
        }
    )
    return sorted_buys


def accumulate_buys(sorted_buys, cum_sold):
    for buy in sorted_buys:
        cum_sold["common"] += buy["common_sold"]
        cum_sold["premium"] += buy["premium_sold"]
        cum_sold["ultra"] += buy["ultra_sold"]

        buy["cum_common_sold"] = cum_sold["common"]
        buy["cum_premium_sold"] = cum_sold["premium"]
        buy["cum_ultra_sold"] = cum_sold["ultra"]

        buy["cum_sold"] = sum([
            cum_sold["common"],
            cum_sold["premium"],
            cum_sold["ultra"]
        ])


def process_buys(new_buys, buy_type, buys, step, now):
    for buy in new_buys:
        timestamp = buy["timestamp"] - buy["timestamp"] % step
        if (str(timestamp) not in buys.keys()):
            buys[str(timestamp)] = {
                "id": timestamp,
                "timestamp": timestamp,
                "timestamp_ms": timestamp * 1000,
                "updated": now,
                "common_sold": 0,
                "premium_sold": 0,
                "ultra_sold": 0,
            }

        buys[str(timestamp)][f"{buy_type}_sold"] += buy["qty"]
