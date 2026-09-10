# 🗄️ LeetCode SQL & Database Solutions

A curated collection of SQL solutions to **LeetCode Database** challenges, maintained for coursework, interview preparation, and mastery of relational database design and advanced querying techniques.

<!-- BADGES:START -->
[![Solved](https://img.shields.io/badge/Solved-9-2563EB?style=for-the-badge&logo=leetcode&logoColor=white)](https://github.com/Saisrikar20/DBMS) [![Easy](https://img.shields.io/badge/Easy-9-22C55E?style=for-the-badge)](https://github.com/Saisrikar20/DBMS) [![Medium](https://img.shields.io/badge/Medium-0-F59E0B?style=for-the-badge)](https://github.com/Saisrikar20/DBMS) [![Hard](https://img.shields.io/badge/Hard-0-EF4444?style=for-the-badge)](https://github.com/Saisrikar20/DBMS) [![Database](https://img.shields.io/badge/Dialect-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://github.com/Saisrikar20/DBMS) [![Views](https://komarev.com/ghpvc/?username=Saisrikar20-DBMS&label=Views&color=0e75b6&style=for-the-badge)](https://github.com/Saisrikar20/DBMS)
<!-- BADGES:END -->

---

## 📌 Overview

This repository tracks solutions to LeetCode database problems. Each accepted submission is systematically synchronized and cataloged, providing a clean reference of SQL queries, edge cases, and query patterns across MySQL.

- **Dialect:** MySQL 8.0 (LeetCode standard)
- **Automatic Sync:** Connected to LeetCode submissions with automatic count and index updates via GitHub Actions CI.
- **Organization:** Each problem is contained in an isolated directory with its problem statement (`README.md`) and optimal SQL query (`*.sql`).

---

## 📊 Progress Dashboard

<!-- STATS:START -->
| Difficulty | Solved | Share of Solutions |
|:---|:---:|:---|
| 🟢 **Easy** | **9** | `██████████` 100% |
| 🟡 **Medium** | **0** | `░░░░░░░░░░` 0% |
| 🔴 **Hard** | **0** | `░░░░░░░░░░` 0% |
| 🎯 **Total** | **9** | `██████████` 100% |
<!-- STATS:END -->

---

## 📑 Problem Index

The table below is **automatically generated and updated** whenever new solutions are added:

<!-- PROBLEMS_TABLE:START -->
| # | Problem Title | Solution | Difficulty | SQL Concepts / Topics |
|:---:|:---|:---:|:---:|:---|
| 577 | [Employee Bonus](https://leetcode.com/problems/employee-bonus) | [💻 SQL](./577-employee-bonus/employee-bonus.sql) | <img src="https://img.shields.io/badge/-Easy-brightgreen?style=flat-square" alt="Easy"> | `LEFT JOIN`, `NULL Handling` |
| 584 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee) | [💻 SQL](./584-find-customer-referee/find-customer-referee.sql) | <img src="https://img.shields.io/badge/-Easy-brightgreen?style=flat-square" alt="Easy"> | `NULL Handling` |
| 595 | [Big Countries](https://leetcode.com/problems/big-countries) | [💻 SQL](./595-big-countries/big-countries.sql) | <img src="https://img.shields.io/badge/-Easy-brightgreen?style=flat-square" alt="Easy"> | `Basic Filtering (WHERE)` |
| 620 | [Not Boring Movies](https://leetcode.com/problems/not-boring-movies) | [💻 SQL](./620-not-boring-movies/not-boring-movies.sql) | <img src="https://img.shields.io/badge/-Easy-brightgreen?style=flat-square" alt="Easy"> | `ORDER BY` |
| 1258 | [Article Views I](https://leetcode.com/problems/article-views-i) | [💻 SQL](./1258-article-views-i/article-views-i.sql) | <img src="https://img.shields.io/badge/-Easy-brightgreen?style=flat-square" alt="Easy"> | `ORDER BY`, `DISTINCT` |
| 1670 | [Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition) | [💻 SQL](./1670-patients-with-a-condition/patients-with-a-condition.sql) | <img src="https://img.shields.io/badge/-Easy-brightgreen?style=flat-square" alt="Easy"> | `Pattern Matching (LIKE)` |
| 1908 | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products) | [💻 SQL](./1908-recyclable-and-low-fat-products/recyclable-and-low-fat-products.sql) | <img src="https://img.shields.io/badge/-Easy-brightgreen?style=flat-square" alt="Easy"> | `Basic Filtering (WHERE)` |
| 3782 | [Find Valid Emails](https://leetcode.com/problems/find-valid-emails) | [💻 SQL](./3782-find-valid-emails/find-valid-emails.sql) | <img src="https://img.shields.io/badge/-Easy-brightgreen?style=flat-square" alt="Easy"> | `ORDER BY`, `REGEXP` |
| 3910 | [Find Books with No Available Copies](https://leetcode.com/problems/find-books-with-no-available-copies) | [💻 SQL](./3910-find-books-with-no-available-copies/find-books-with-no-available-copies.sql) | <img src="https://img.shields.io/badge/-Easy-brightgreen?style=flat-square" alt="Easy"> | `GROUP BY`, `HAVING`, `ORDER BY`, `NULL Handling` |
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
  <sub>Maintained by <a href="https://github.com/Saisrikar20">Saisrikar</a> • Built with Python & GitHub Actions</sub>
</div>
