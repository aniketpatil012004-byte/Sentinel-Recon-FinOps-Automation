import os
import random
from fpdf import FPDF

# Ensure sub-folder exists
if not os.path.exists("Bank_Statements"):
    os.makedirs("Bank_Statements")

def generate_noisy_data(num_files):
    print(f"Generating {num_files} high-noise PDFs...")
    noise_sentences = [
        "This document is strictly confidential and for the recipient only.",
        "Terms and conditions apply as per the Master Service Agreement.",
        "Bank of India - Treasury Operations Division - Mumbai Branch.",
        "Processed by automated system on behalf of the settlement team.",
        "Please contact support@bank.com for any discrepancies."
    ]

    for i in range(num_files):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        
        txn_id = f"TXN{5000 + i}"
        # Randomized amounts to test our logic
        amt = random.choice([100000, 100000, 95000]) 
        
        # Adding 'Noise' (Extra info)
        pdf.cell(200, 10, txt=random.choice(noise_sentences), ln=True)
        pdf.ln(5)
        pdf.cell(200, 10, txt=f"Official Record for ID: {txn_id}", ln=True)
        pdf.cell(200, 10, txt=random.choice(noise_sentences), ln=True)
        pdf.cell(200, 10, txt=f"Total Settled Amount: INR {amt}", ln=True)
        pdf.cell(200, 10, txt="End of Statement.", ln=True)
        
        pdf.output(f"Bank_Statements/Statement_{txn_id}.pdf")
    print("✅ 1,000 PDFs Generated!")

if __name__ == "__main__":
    generate_bank_data = generate_noisy_data(1000)