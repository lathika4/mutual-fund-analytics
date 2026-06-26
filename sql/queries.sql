-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM 07_scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT
strftime('%Y-%m', date) AS Month,
AVG(nav) AS Average_NAV
FROM 02_nav_history
GROUP BY Month
ORDER BY Month;

-- 3. Total SIP Amount
SELECT SUM(amount_inr) AS Total_SIP
FROM 08_investor_transactions
WHERE transaction_type='Sip';

-- 4. Transactions by State
SELECT state, COUNT(*) AS Total_Transactions
FROM 08_investor_transactions
GROUP BY state
ORDER BY Total_Transactions DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM 07_scheme_performance
WHERE expense_ratio_pct < 1;

-- 6. Top 5 Returns (5 Years)
SELECT scheme_name, return_5yr_pct
FROM 07_scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 7. Average Returns by Category
SELECT category,
AVG(return_3yr_pct) AS Avg_Return
FROM 07_scheme_performance
GROUP BY category;

-- 8. Transactions by Payment Mode
SELECT payment_mode,
COUNT(*) AS Total
FROM 08_investor_transactions
GROUP BY payment_mode;

-- 9. Funds by Risk Grade
SELECT risk_grade,
COUNT(*) AS Total
FROM 07_scheme_performance
GROUP BY risk_grade;

-- 10. Top Fund Houses by Number of Schemes
SELECT fund_house,
COUNT(*) AS Schemes
FROM 01_fund_master
GROUP BY fund_house
ORDER BY Schemes DESC;