
# PLP Data Analytics Assignment 3
## Duka Sales and Agent Cleanup

**Student:** Christine Wanjira

## Project Overview

This project contains two data analytics engagements:

1. Duka Electronics Sales Exploration.
2. Agent Transactions Data Cleaning and Quality Assessment.

## Engagement 1: Duka Electronics Sales Exploration

The first engagement analyses 1,000 Duka Electronics sales orders from five branches between January and June 2026.

The analysis explores branch performance, product revenue, monthly trends, weekday and weekend sales, and price categories.

### Executive Summary

The Duka Electronics dataset contains 1,000 sales orders from 5 branches between January and June 2026. Nairobi recorded the highest branch revenue of KES 26,106,100. Laptops generated the highest product revenue of KES 41,535,000. April recorded the highest monthly revenue of KES 13,518,300, while June recorded the lowest at KES 10,903,400. The filtered dataset contained 83 Premium Online orders from Nairobi and Mombasa, generating total revenue of KES 10,218,000.

### Duka Output Files

- `excel/duka_branch_summary.xlsx`
- `outputs/premium_online_coast_capital.csv`

## Engagement 2: Agent Transactions Cleanup

The second engagement focuses on cleaning agent transaction data, identifying data quality issues and preparing reliable data for analysis.

The cleaning pipeline performs the following tasks:

- Removes duplicate transaction IDs.
- Standardises transaction types.
- Converts transaction amounts to numeric values.
- Imputes missing amounts using the median.
- Flags potential outliers using the IQR method.
- Standardises transaction dates.
- Merges agent county information.

### Agent Data Before and After Cleaning

- Original transaction rows: 612
- Duplicate rows removed: 12
- Final cleaned transaction rows: 600
- Unknown agent transactions after cleaning: 7

### Agent Output File

- `outputs/agent_transactions_clean.csv`

## Project Files

- `generate_data.py` - Generates the Duka and agent datasets.
- `cleaning_pipeline.py` - Contains the agent data cleaning function.
- `duka_sales_exploration.ipynb` - Duka sales analysis.
- `agent_cleanup.ipynb` - Agent data cleaning and quality report.
- `requirements.txt` - Required Python libraries.
- `excel/` - Excel analysis workbook.
- `outputs/` - Final exported datasets.

## How to Run the Project

### 1. Install Requirements

```bash
pip install -r requirements.txt
