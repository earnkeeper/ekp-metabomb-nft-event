def documents(usdRate, mtbRate, fiat_symbol):
    return [
        {
            "id": 'normal',
            "box": 'Normal',
            "quantity": 5000,
            "staking": 3000,
            "stakeCost": round(3000 * mtbRate, 2),
            "cost": round(19.99 * usdRate, 2),
            "totalCost": round(19.99 * usdRate + 3000 * mtbRate, 2),
            "maxCost": round(19.99 * usdRate + 3000 * mtbRate * 4, 2),
            "limit": 4,
            "fiatSymbol": fiat_symbol,
            "mtbRate": mtbRate,
            "rarities": "Common 90%, Rare 10%"
        },
        {
            "id": 'premium',
            "box": 'Premium',
            "quantity": 2000,
            "staking": 10000,
            "stakeCost": round(10000 * mtbRate, 2),
            "totalCost": round(99.99 * usdRate + 10000 * mtbRate, 2),
            "maxCost": round(99.99 * usdRate + 10000 * mtbRate * 2, 2),
            "cost": round(99.99 * usdRate, 2),
            "limit": 2,
            "fiatSymbol": fiat_symbol,
            "mtbRate": mtbRate,
            "rarities": "Common 50%, Rare 40%, Epic 9%, Legend 1%"
        },
        {
            "id": 'ultra',
            "box": 'Ultra',
            "quantity": 1000,
            "staking": 50000,
            "stakeCost": round(50000 * mtbRate, 2),
            "totalCost": round(499.99 * usdRate + 50000 * mtbRate, 2),
            "maxCost": round(499.99 * usdRate + 50000 * mtbRate * 1, 2),
            "cost": round(499.99 * usdRate, 2),
            "limit": 1,
            "fiatSymbol": fiat_symbol,
            "mtbRate": mtbRate,
            "rarities": "Rare 55%, Epic 40%, Legend 4.9%, Mythic 0.1%"
        }
    ]
