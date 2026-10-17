# 🗄️ LeetCode SQL & Database Solutions

A curated collection of SQL solutions to **LeetCode Database** challenges, maintained for coursework, interview preparation, and mastery of relational database design and advanced querying techniques.

<!-- BADGES:START -->
[![LeetCode Profile](https://img.shields.io/badge/LeetCode-rTP0FaRcOa-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/rTP0FaRcOa/) [![Solved](https://img.shields.io/badge/Solved-49-2563EB?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/rTP0FaRcOa/) [![Easy](https://img.shields.io/badge/Easy-25-22C55E?style=for-the-badge)](https://leetcode.com/u/rTP0FaRcOa/) [![Medium](https://img.shields.io/badge/Medium-17-F59E0B?style=for-the-badge)](https://leetcode.com/u/rTP0FaRcOa/) [![Hard](https://img.shields.io/badge/Hard-7-EF4444?style=for-the-badge)](https://leetcode.com/u/rTP0FaRcOa/) [![Database](https://img.shields.io/badge/Dialect-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://github.com/Saisrikar20/DBMS) [![Views](https://komarev.com/ghpvc/?username=Saisrikar20-DBMS&label=Views&color=0e75b6&style=for-the-badge)](https://github.com/Saisrikar20/DBMS)
<!-- BADGES:END -->

---

## 📌 Overview

This repository automatically tracks and synchronizes my database practice questions directly from my LeetCode profile: [**@rTP0FaRcOa**](https://leetcode.com/u/rTP0FaRcOa/) using the LeetCode Sync extension. Each accepted submission is committed automatically, reflecting an active history of problems attempted and mastered.

- **LeetCode Profile:** [leetcode.com/u/rTP0FaRcOa](https://leetcode.com/u/rTP0FaRcOa/)
- **SQL Dialect:** MySQL 8.0 (LeetCode standard)
- **Automatic Sync:** Connected to LeetCode submissions with automatic count and index updates via GitHub Actions CI.
- **Organization:** Each problem is contained in an isolated directory with its problem statement (`README.md`) and optimal SQL query (`*.sql`).

---

## 📊 Progress Dashboard

<!-- STATS:START -->
| Difficulty | Solved | Share of Solutions |
|:---|:---:|:---|
| 🟢 **Easy** | **25** | `█████░░░░░` 51% |
| 🟡 **Medium** | **17** | `███░░░░░░░` 34% |
| 🔴 **Hard** | **7** | `█░░░░░░░░░` 14% |
| 🎯 **Total** | **49** | `██████████` 100% |
<!-- STATS:END -->

---

## 📑 Problem Index

The table below is **automatically generated and updated** whenever new solutions are added:

<!-- PROBLEMS_TABLE:START -->
> 💡 **Tip:** Solutions are grouped into collapsible drawers below. Click any section to expand or collapse. For the full master list, see [`SOLUTIONS.md`](./SOLUTIONS.md).

<details open>
<summary><b>🟢 Easy Problems (25)</b> — <i>Click to expand/collapse</i></summary>

| # | Problem Title | Solution | SQL Concepts / Topics |
|:---:|:---|:---:|:---|
| 196 | [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails) | [💻 SQL](./196-delete-duplicate-emails/delete-duplicate-emails.sql) | `GROUP BY` |
| 197 | [Rising Temperature](https://leetcode.com/problems/rising-temperature) | [💻 SQL](./197-rising-temperature/rising-temperature.sql) | `INNER JOIN` |
| 577 | [Employee Bonus](https://leetcode.com/problems/employee-bonus) | [💻 SQL](./577-employee-bonus/employee-bonus.sql) | `LEFT JOIN`, `NULL Handling` |
| 584 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee) | [💻 SQL](./584-find-customer-referee/find-customer-referee.sql) | `NULL Handling` |
| 595 | [Big Countries](https://leetcode.com/problems/big-countries) | [💻 SQL](./595-big-countries/big-countries.sql) | `Basic Filtering (WHERE)` |
| 596 | [Classes With at Least 5 Students](https://leetcode.com/problems/classes-with-at-least-5-students) | [💻 SQL](./596-classes-with-at-least-5-students/classes-with-at-least-5-students.sql) | `GROUP BY`, `HAVING` |
| 620 | [Not Boring Movies](https://leetcode.com/problems/not-boring-movies) | [💻 SQL](./620-not-boring-movies/not-boring-movies.sql) | `ORDER BY` |
| 627 | [Swap Sex of Employees](https://leetcode.com/problems/swap-sex-of-employees) | [💻 SQL](./627-swap-sex-of-employees/swap-sex-of-employees.sql) | `CASE WHEN` |
| 1153 | [Product Sales Analysis I](https://leetcode.com/problems/product-sales-analysis-i) | [💻 SQL](./1153-product-sales-analysis-i/product-sales-analysis-i.sql) | `INNER JOIN` |
| 1245 | [User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i) | [💻 SQL](./1245-user-activity-for-the-past-30-days-i/user-activity-for-the-past-30-days-i.sql) | `GROUP BY`, `DISTINCT` |
| 1258 | [Article Views I](https://leetcode.com/problems/article-views-i) | [💻 SQL](./1258-article-views-i/article-views-i.sql) | `ORDER BY`, `DISTINCT` |
| 1509 | [Replace Employee ID With The Unique Identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier) | [💻 SQL](./1509-replace-employee-id-with-the-unique-identifier/replace-employee-id-with-the-unique-identifier.sql) | `RIGHT JOIN` |
| 1625 | [Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date) | [💻 SQL](./1625-group-sold-products-by-the-date/group-sold-products-by-the-date.sql) | `GROUP BY`, `ORDER BY`, `DISTINCT` |
| 1670 | [Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition) | [💻 SQL](./1670-patients-with-a-condition/patients-with-a-condition.sql) | `Pattern Matching (LIKE)` |
| 1724 | [Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions) | [💻 SQL](./1724-customer-who-visited-but-did-not-make-any-transactions/customer-who-visited-but-did-not-make-any-transactions.sql) | `RIGHT JOIN`, `GROUP BY`, `NULL Handling` |
| 1734 | [Bank Account Summary II](https://leetcode.com/problems/bank-account-summary-ii) | [💻 SQL](./1734-bank-account-summary-ii/bank-account-summary-ii.sql) | `GROUP BY`, `HAVING` |
| 1801 | [Average Time of Process per Machine](https://leetcode.com/problems/average-time-of-process-per-machine) | [💻 SQL](./1801-average-time-of-process-per-machine/average-time-of-process-per-machine.sql) | `GROUP BY` |
| 1827 | [Invalid Tweets](https://leetcode.com/problems/invalid-tweets) | [💻 SQL](./1827-invalid-tweets/invalid-tweets.sql) | `Basic Filtering (WHERE)` |
| 1837 | [Daily Leads and Partners](https://leetcode.com/problems/daily-leads-and-partners) | [💻 SQL](./1837-daily-leads-and-partners/daily-leads-and-partners.sql) | `GROUP BY`, `ORDER BY`, `DISTINCT` |
| 1908 | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products) | [💻 SQL](./1908-recyclable-and-low-fat-products/recyclable-and-low-fat-products.sql) | `Basic Filtering (WHERE)` |
| 2041 | [The Latest Login in 2020](https://leetcode.com/problems/the-latest-login-in-2020) | [💻 SQL](./2041-the-latest-login-in-2020/the-latest-login-in-2020.sql) | `GROUP BY` |
| 2495 | [Number of Unique Subjects Taught by Each Teacher](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher) | [💻 SQL](./2495-number-of-unique-subjects-taught-by-each-teacher/number-of-unique-subjects-taught-by-each-teacher.sql) | `GROUP BY`, `DISTINCT` |
| 3782 | [Find Valid Emails](https://leetcode.com/problems/find-valid-emails) | [💻 SQL](./3782-find-valid-emails/find-valid-emails.sql) | `ORDER BY`, `REGEXP` |
| 3910 | [Find Books with No Available Copies](https://leetcode.com/problems/find-books-with-no-available-copies) | [💻 SQL](./3910-find-books-with-no-available-copies/find-books-with-no-available-copies.sql) | `GROUP BY`, `HAVING`, `ORDER BY`, `NULL Handling` |
| 4195 | [Find Users with High Token Usage](https://leetcode.com/problems/find-users-with-high-token-usage) | [💻 SQL](./4195-find-users-with-high-token-usage/find-users-with-high-token-usage.sql) | `GROUP BY`, `HAVING`, `ORDER BY` |

</details>

<details open>
<summary><b>🟡 Medium Problems (17)</b> — <i>Click to expand/collapse</i></summary>

| # | Problem Title | Solution | SQL Concepts / Topics |
|:---:|:---|:---:|:---|
| 570 | [Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports) | [💻 SQL](./570-managers-with-at-least-5-direct-reports/managers-with-at-least-5-direct-reports.sql) | `GROUP BY`, `HAVING`, `NULL Handling` |
| 602 | [Friend Requests II: Who Has the Most Friends](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends) | [💻 SQL](./602-friend-requests-ii-who-has-the-most-friends/friend-requests-ii-who-has-the-most-friends.sql) | `GROUP BY`, `ORDER BY`, `UNION` |
| 608 | [Tree Node](https://leetcode.com/problems/tree-node) | [💻 SQL](./608-tree-node/tree-node.sql) | `NULL Handling`, `CASE WHEN` |
| 1135 | [Customers Who Bought All Products](https://leetcode.com/problems/customers-who-bought-all-products) | [💻 SQL](./1135-customers-who-bought-all-products/customers-who-bought-all-products.sql) | `GROUP BY`, `HAVING`, `DISTINCT` |
| 1155 | [Product Sales Analysis III](https://leetcode.com/problems/product-sales-analysis-iii) | [💻 SQL](./1155-product-sales-analysis-iii/product-sales-analysis-iii.sql) | `GROUP BY` |
| 1292 | [Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii) | [💻 SQL](./1292-immediate-food-delivery-ii/immediate-food-delivery-ii.sql) | `GROUP BY` |
| 1327 | [Last Person to Fit in the Bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus) | [💻 SQL](./1327-last-person-to-fit-in-the-bus/last-person-to-fit-in-the-bus.sql) | `ORDER BY`, `Aggregation` |
| 3848 | [Analyze Subscription Conversion](https://leetcode.com/problems/analyze-subscription-conversion) | [💻 SQL](./3848-analyze-subscription-conversion/analyze-subscription-conversion.sql) | `GROUP BY`, `HAVING`, `ORDER BY`, `CASE WHEN` |
| 3865 | [Find Product Recommendation Pairs](https://leetcode.com/problems/find-product-recommendation-pairs) | [💻 SQL](./3865-find-product-recommendation-pairs/find-product-recommendation-pairs.sql) | `GROUP BY`, `HAVING`, `ORDER BY`, `DISTINCT` |
| 3898 | [Seasonal Sales Analysis](https://leetcode.com/problems/seasonal-sales-analysis) | [💻 SQL](./3898-seasonal-sales-analysis/seasonal-sales-analysis.sql) | `INNER JOIN`, `GROUP BY`, `ORDER BY`, `Window Functions`, `CASE WHEN` |
| 3932 | [Find COVID Recovery Patients](https://leetcode.com/problems/find-covid-recovery-patients) | [💻 SQL](./3932-find-covid-recovery-patients/find-covid-recovery-patients.sql) | `GROUP BY`, `ORDER BY` |
| 3942 | [Find Drivers with Improved Fuel Efficiency](https://leetcode.com/problems/find-drivers-with-improved-fuel-efficiency) | [💻 SQL](./3942-find-drivers-with-improved-fuel-efficiency/find-drivers-with-improved-fuel-efficiency.sql) | `GROUP BY`, `HAVING`, `ORDER BY`, `CASE WHEN` |
| 3943 | [Find Overbooked Employees](https://leetcode.com/problems/find-overbooked-employees) | [💻 SQL](./3943-find-overbooked-employees/find-overbooked-employees.sql) | `GROUP BY`, `HAVING`, `ORDER BY` |
| 3971 | [Find Stores with Inventory Imbalance](https://leetcode.com/problems/find-stores-with-inventory-imbalance) | [💻 SQL](./3971-find-stores-with-inventory-imbalance/find-stores-with-inventory-imbalance.sql) | `INNER JOIN`, `GROUP BY`, `ORDER BY`, `Window Functions`, `CASE WHEN` |
| 3996 | [Find Books with Polarized Opinions](https://leetcode.com/problems/find-books-with-polarized-opinions) | [💻 SQL](./3996-find-books-with-polarized-opinions/find-books-with-polarized-opinions.sql) | `GROUP BY`, `HAVING`, `ORDER BY`, `CASE WHEN` |
| 4091 | [Find Golden Hour Customers](https://leetcode.com/problems/find-golden-hour-customers) | [💻 SQL](./4091-find-golden-hour-customers/find-golden-hour-customers.sql) | `GROUP BY`, `HAVING`, `ORDER BY`, `CASE WHEN` |
| 4208 | [Find Emotionally Consistent Users](https://leetcode.com/problems/find-emotionally-consistent-users) | [💻 SQL](./4208-find-emotionally-consistent-users/find-emotionally-consistent-users.sql) | `GROUP BY`, `ORDER BY`, `Window Functions` |

</details>

<details open>
<summary><b>🔴 Hard Problems (7)</b> — <i>Click to expand/collapse</i></summary>

| # | Problem Title | Solution | SQL Concepts / Topics |
|:---:|:---|:---:|:---|
| 185 | [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries) | [💻 SQL](./185-department-top-three-salaries/department-top-three-salaries.sql) | `INNER JOIN`, `ORDER BY`, `Window Functions` |
| 262 | [Trips and Users](https://leetcode.com/problems/trips-and-users) | [💻 SQL](./262-trips-and-users/trips-and-users.sql) | `GROUP BY`, `CASE WHEN` |
| 601 | [Human Traffic of Stadium](https://leetcode.com/problems/human-traffic-of-stadium) | [💻 SQL](./601-human-traffic-of-stadium/human-traffic-of-stadium.sql) | `GROUP BY`, `HAVING`, `ORDER BY`, `Window Functions` |
| 3891 | [Find Category Recommendation Pairs](https://leetcode.com/problems/find-category-recommendation-pairs) | [💻 SQL](./3891-find-category-recommendation-pairs/find-category-recommendation-pairs.sql) | `GROUP BY`, `HAVING`, `ORDER BY`, `DISTINCT` |
| 4043 | [Find Zombie Sessions](https://leetcode.com/problems/find-zombie-sessions) | [💻 SQL](./4043-find-zombie-sessions/find-zombie-sessions.sql) | `GROUP BY`, `HAVING`, `ORDER BY` |
| 4169 | [Most Common Course Pairs](https://leetcode.com/problems/most-common-course-pairs) | [💻 SQL](./4169-most-common-course-pairs/most-common-course-pairs.sql) | `INNER JOIN`, `GROUP BY`, `HAVING`, `ORDER BY`, `NULL Handling`, `Window Functions` |
| 4227 | [Find Users with Persistent Behavior Patterns](https://leetcode.com/problems/find-users-with-persistent-behavior-patterns) | [💻 SQL](./4227-find-users-with-persistent-behavior-patterns/find-users-with-persistent-behavior-patterns.sql) | `GROUP BY`, `HAVING`, `ORDER BY`, `Window Functions` |

</details>
<!-- PROBLEMS_TABLE:END -->

---

## 🧠 Topics & SQL Techniques Covered

- **Filtering & Predicates:** `WHERE`, `AND`, `OR`, `IN`, `BETWEEN`, modulo arithmetic, conditional ordering.
- **Pattern Matching & Regular Expressions:** `LIKE`, wildcard searching, MySQL `REGEXP` for strict string and email validation.
- **Three-Valued Logic & NULL Handling:** Safe null checks (`IS NULL`, `IS NOT NULL`), `IFNULL()`, `COALESCE()`.
- **Joins & Set Operations:** `INNER JOIN`, `LEFT JOIN` for preserving unmatched records, `UNION` / `UNION ALL`.
- **Aggregations & Grouping:** `COUNT()`, `SUM()`, `AVG()`, `GROUP BY`, and post-aggregation filtering with `HAVING`.
- **Advanced Querying:** Common Table Expressions (`WITH`), subqueries, and window functions (`ROW_NUMBER()`, `DENSE_RANK()`, `OVER()`).

---

## 📂 Repository Structure

```
DBMS/
├── .github/
│   └── workflows/
│       └── update_readme.yml      # CI/CD workflow for automated counter & table generation
├── scripts/
│   └── update_readme.py           # Python script that counts solutions and syncs README.md
├── <problem-id>-<slug>/           # Problem directory
│   ├── README.md                  # Problem description and examples from LeetCode
│   └── <slug>.sql                 # Accepted SQL solution
└── README.md                      # Repository overview, dynamic stats, and problem index
```

---

## ⚡ Automation & Local Usage

This repository features an **automated counting program**:

### 1. Automatic GitHub Actions CI
Whenever a new solution is committed (via LeetCode Sync or git push), the [GitHub Actions Workflow](.github/workflows/update_readme.yml) triggers automatically:
1. Discovers all problem folders and SQL solutions.
2. Extracts problem titles, links, and difficulty classifications.
3. Automatically increments the total, Easy, Medium, and Hard counters.
4. Generates the formatted markdown table and updates `README.md`.
5. Commits and pushes the update automatically.

### 2. Run Manually / Locally
You can also run the count updater locally anytime:

```bash
python scripts/update_readme.py
```

---

<div align="center">
  <sub>Maintained by <a href="https://github.com/Saisrikar20">Saisrikar</a> • LeetCode: <a href="https://leetcode.com/u/rTP0FaRcOa/">@rTP0FaRcOa</a> • Built with Python & GitHub Actions</sub>
</div>
