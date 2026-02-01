# Sentinel-Recon: Scalable Treasury Automation

## 📌 Project Overview
As a CFA/FRM candidate, I developed this project to simulate a high-volume Treasury Operations environment. The system automates the reconciliation of 1,000+ unstructured bank advices (PDFs) against an internal ledger (CSV).

## 🚀 Key Performance Metrics
* **Volume:** 1,000 Transactions processed.
* **Speed:** ~3.1 seconds using Parallel Processing (4 CPU cores).
* **Accuracy:** 100% detection of financial "breaks" (discrepancies).

## 🛠️ Tech Stack
* **Python 3.x:** Core logic and automation.
* **Multiprocessing:** Parallel core execution for high-speed data parsing.
* **Regex (re):** Pattern matching to extract metadata from "noisy" PDFs.
* **Pandas:** Data manipulation and exception reporting.

## 📁 Repository Structure
* `1_generator.py`: Generates 1,000 synthetic bank PDFs with random discrepancies.
* `2_ledger.py`: Creates the 'Gold Standard' internal ledger for comparison.
* `3_reconciler.py`: The master engine that identifies and reports breaks.<img width="850" height="200" alt="Screenshot 2026-02-01 203441" src="https://github.com/user-attachments/assets/3e27bff4-f3c5-4631-82cd-deb7614f6902" />
