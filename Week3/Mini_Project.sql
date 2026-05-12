WITH ranked_transactions AS (
    SELECT 
        transaction_id,
        customer_id,
        status,
        amount,
        updated_at,
        source_system,

        -- Step 1: Identify latest record per transaction
        ROW_NUMBER() OVER (
            PARTITION BY transaction_id
            ORDER BY updated_at DESC
        ) AS rn,

        -- Step 2: Track status changes over time
        LAG(status) OVER (
            PARTITION BY transaction_id
            ORDER BY updated_at
        ) AS previous_status

    FROM transactions
    -- Step 3: Basic performance filtering (reduce scanned data early)
    WHERE source_system = 'core'
      AND updated_at >= DATE '2024-01-01'
)

-- Step 4: Keep only latest valid transaction record
SELECT 
    transaction_id,
    customer_id,
    status,
    amount,
    updated_at,
    source_system,
    previous_status
FROM ranked_transactions
WHERE rn = 1;