import os
import re
import pandas as pd
from pypdf import PdfReader
from multiprocessing import Pool, cpu_count
import time

# 1. SETUP: Load Ledger into memory for fast access
ledger = pd.read_csv('internal_ledger.csv')
expected_data = dict(zip(ledger['Transaction_ID'].astype(str), ledger['Expected_Amount']))

def process_single_pdf(filename):
    """Function to parse one PDF and check against the ledger"""
    try:
        path = os.path.join('Bank_Statements', filename)
        reader = PdfReader(path)
        text = " ".join([page.extract_text() for page in reader.pages])
        
        # Sniper Regex: We ignore all the 'Noise' and just find the ID and INR
        txn_id_match = re.search(r"TXN\d+", text)
        amount_match = re.search(r"INR\s?(\d+)", text)
        
        if txn_id_match and amount_match:
            tid = txn_id_match.group(0)
            amt = float(amount_match.group(1))
            
            expected = expected_data.get(tid)
            if expected is None:
                return {"ID": tid, "Status": "NOT_IN_LEDGER", "Diff": 0}
            elif amt == expected:
                return {"ID": tid, "Status": "MATCH", "Diff": 0}
            else:
                return {"ID": tid, "Status": "BREAK", "Diff": expected - amt}
    except Exception as e:
        return {"ID": filename, "Status": f"ERROR: {e}", "Diff": 0}
    return None

if __name__ == "__main__":
    print(f"🚀 Starting High-Volume Recon on {cpu_count()} CPU cores...")
    start_time = time.time()
    
    # Get all PDF filenames
    files = [f for f in os.listdir('Bank_Statements') if f.endswith('.pdf')]
    
    # 2. MULTIPROCESSING: Run extraction on all cores at once
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_single_pdf, files)
    
    # Filter out any None results and create a Report
    results = [r for r in results if r is not None]
    df_results = pd.DataFrame(results)
    
    # 3. EXPORT: Save the 'Breaks' to a specialized Excel file
    breaks = df_results[df_results['Status'] == 'BREAK']
    breaks.to_excel("Treasury_Exceptions_Report.xlsx", index=False)
    
    end_time = time.time()
    print(f"\n✅ FINISHED in {round(end_time - start_time, 2)} seconds!")
    print(f"Total Files: {len(df_results)}")
    print(f"Total Breaks Found: {len(breaks)}")
    print("📁 Open 'Treasury_Exceptions_Report.xlsx' to see the errors.")