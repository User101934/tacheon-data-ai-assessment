

from fetch_data import fetch_crypto_data
from transform import transform_data
from load_bigquery import load_to_bigquery

def main():

    raw_data = fetch_crypto_data()

    transformed_df = transform_data(raw_data)

    print(transformed_df.head())

    load_to_bigquery(transformed_df)

if __name__ == "__main__":
    main()
