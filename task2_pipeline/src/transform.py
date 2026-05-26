import pandas as pd

def transform_data(data):

    df = pd.json_normalize(data)

    selected_columns = [
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"
    ]

    df = df[selected_columns]

    df.columns = [
        "coin_id",
        "symbol",
        "coin_name",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_24h"
    ]

    df["market_status"] = df["price_change_24h"].apply(
        lambda x: "Growing" if x > 0 else "Declining"
    )

    df["volume_to_marketcap_ratio"] = (
        df["total_volume"] / df["market_cap"]
    )

    return df
