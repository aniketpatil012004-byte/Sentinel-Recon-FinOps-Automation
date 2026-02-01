import pandas as pd

# Ledger expects 100,000 for all 1,000 transactions
data = {
    'Transaction_ID': [f"TXN{5000 + i}" for i in range(1000)],
    'Expected_Amount': [100000] * 1000 
}

df = pd.DataFrame(data)
df.to_csv('internal_ledger.csv', index=False)
print("✅ internal_ledger.csv created with 1,000 rows!")