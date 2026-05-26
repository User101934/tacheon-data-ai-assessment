
SELECT
    market_status,
    COUNT(*) AS total_coins,
    AVG(current_price) AS avg_price,
    AVG(volume_to_marketcap_ratio) AS avg_volume_ratio
FROM `project-497511.crypto_pipeline.crypto_market`
GROUP BY market_status
ORDER BY avg_price DESC;
