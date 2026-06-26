# Mutual Fund Analytics - Data Dictionary

## 1. Fund Master (01_fund_master.csv)

| Column             | Data Type | Description                                  |
| ------------------ | --------- | -------------------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme code                      |
| fund_house         | Text      | Mutual fund company                          |
| scheme_name        | Text      | Name of the mutual fund scheme               |
| category           | Text      | Fund category (Equity, Debt, etc.)           |
| sub_category       | Text      | Specific category (Large Cap, Mid Cap, etc.) |
| plan               | Text      | Direct or Regular                            |
| launch_date        | Date      | Scheme launch date                           |
| benchmark          | Text      | Benchmark index                              |
| expense_ratio_pct  | Decimal   | Expense ratio (%)                            |
| exit_load_pct      | Decimal   | Exit load (%)                                |
| min_sip_amount     | Integer   | Minimum SIP investment                       |
| min_lumpsum_amount | Integer   | Minimum lump sum investment                  |
| fund_manager       | Text      | Fund manager name                            |
| risk_category      | Text      | Risk level                                   |
| sebi_category_code | Text      | SEBI category code                           |

---

## 2. NAV History (02_nav_history.csv)

| Column    | Data Type | Description      |
| --------- | --------- | ---------------- |
| amfi_code | Integer   | AMFI scheme code |
| date      | Date      | NAV date         |
| nav       | Decimal   | Net Asset Value  |

---

## 3. AUM by Fund House (03_aum_by_fund_house.csv)

Contains monthly Assets Under Management (AUM) for each fund house.

---

## 4. Monthly SIP Inflows (04_monthly_sip_inflows.csv)

Contains monthly SIP inflow data.

---

## 5. Category Inflows (05_category_inflows.csv)

Contains category-wise inflows.

---

## 6. Industry Folio Count (06_industry_folio_count.csv)

Contains folio counts across the mutual fund industry.

---

## 7. Scheme Performance (07_scheme_performance.csv)

Contains fund returns, alpha, beta, Sharpe ratio, expense ratio, AUM and ratings.

---

## 8. Investor Transactions (08_investor_transactions.csv)

Contains investor transaction records including SIP, Lumpsum and Redemption.

---

## 9. Portfolio Holdings (09_portfolio_holdings.csv)

Contains portfolio holdings and stock allocation.

---

## 10. Benchmark Indices (10_benchmark_indices.csv)

Contains benchmark index closing values used for fund comparison.

---

## Data Source

Bluestock Capstone Mutual Fund Analytics Dataset.
