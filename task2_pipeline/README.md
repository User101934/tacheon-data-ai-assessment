
# Task 2 - Data Pipeline

## Overview

This project demonstrates a simple end-to-end data pipeline built using Python and Google BigQuery.

The pipeline fetches cryptocurrency market data from the CoinGecko public API, transforms the data into a more analytics-friendly format, and stores the processed results in BigQuery for querying and analysis.

---

# API Chosen

## CoinGecko API

API Used:
https://api.coingecko.com/api/v3/coins/markets

### Why This API?

I selected the CoinGecko API because:
- It provides structured real-world financial data
- No API key is required
- The response format is suitable for transformation and analytics
- It includes useful market metrics such as prices, market cap, and trading volume

---

# Pipeline Workflow

```text
CoinGecko API
      ↓
Python Fetch Script
      ↓
Data Transformation (Pandas)
      ↓
Derived Analytical Fields
      ↓
BigQuery Storage
      ↓
SQL Analytics Query
```

---

# Features Implemented

## Data Fetching

The pipeline:
- Calls the CoinGecko API
- Retrieves cryptocurrency market data
- Handles API request failures gracefully
- Includes logging for execution tracking

---

## Data Transformation

The raw API response is transformed using pandas.

Transformations include:
- Flattening JSON data
- Renaming columns for readability
- Selecting only useful fields
- Handling structured tabular formatting

---

## Derived Fields

Two analytical fields were added:

### market_status
Classifies each coin as:
- Growing
- Declining

based on 24-hour price movement.

### volume_to_marketcap_ratio
Calculates:
```text
total_volume / market_cap
```

This helps analyze relative trading activity.

---

# BigQuery Setup

The transformed data is loaded into Google BigQuery Sandbox.

Dataset:
```text
crypto_pipeline
```

Table:
```text
crypto_market
```

The pipeline automatically creates and loads the table if it does not already exist.

---

# How To Run

## Install Dependencies

```bash
pip install pandas requests google-cloud-bigquery pyarrow
```

---

## Run Pipeline

```bash
python src/main.py
```

---

# SQL Analysis Query

The following SQL query was used to generate analytical insights:

```sql
SELECT
    market_status,
    COUNT(*) AS total_coins,
    AVG(current_price) AS avg_price,
    AVG(volume_to_marketcap_ratio) AS avg_volume_ratio
FROM `project-497511.crypto_pipeline.crypto_market`
GROUP BY market_status
ORDER BY avg_price DESC;
```

---

# Sample Insight

The query helps identify:
- Number of growing vs declining coins
- Average market prices
- Relative trading activity trends

---

# Production Considerations

## How Would This Pipeline Be Scheduled?

In production, the pipeline could be scheduled using:
- Cron jobs
- Apache Airflow
- Google Cloud Scheduler

A daily scheduled run would likely be sufficient for this use case.

---

## How Would Failures Be Monitored?

Failures could be monitored using:
- Logging systems
- Email alerts
- Cloud monitoring dashboards
- Retry mechanisms for temporary API failures

---

## How Would The Pipeline Scale?

To support larger data volumes:
- Batch processing could be implemented
- Incremental loading strategies could be added
- Partitioned BigQuery tables could improve performance
- Cloud-based orchestration tools could manage scaling automatically

---

# Final Thoughts

The goal of this project was to build a clean, practical, and maintainable data pipeline rather than over-engineer a complex system.

The implementation focuses on:
- reliability
- readability
- modular design
- analytical usefulness
