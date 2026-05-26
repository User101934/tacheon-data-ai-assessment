from google.cloud import bigquery
import logging

logging.basicConfig(level=logging.INFO)

def load_to_bigquery(df):

    client = bigquery.Client.from_service_account_json(
        "project-497511-9d7d340b8d78.json"
    )

    table_id = "project-497511.crypto_pipeline.crypto_market"

    job = client.load_table_from_dataframe(df, table_id)

    job.result()

    logging.info("Data successfully loaded into BigQuery")
