# 🗄️ LeetCode SQL & Database Solutions

A curated collection of SQL solutions to **LeetCode Database** challenges, maintained for coursework, interview preparation, and mastery of relational database design and advanced querying techniques.

<!-- BADGES:START -->
[![LeetCode Profile](https://img.shields.io/badge/LeetCode-rTP0FaRcOa-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/rTP0FaRcOa/) [![Solved](https://img.shields.io/badge/Solved-15-2563EB?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/rTP0FaRcOa/) [![Easy](https://img.shields.io/badge/Easy-14-22C55E?style=for-the-badge)](https://leetcode.com/u/rTP0FaRcOa/) [![Medium](https://img.shields.io/badge/Medium-1-F59E0B?style=for-the-badge)](https://leetcode.com/u/rTP0FaRcOa/) [![Hard](https://img.shields.io/badge/Hard-0-EF4444?style=for-the-badge)](https://leetcode.com/u/rTP0FaRcOa/) [![Database](https://img.shields.io/badge/Dialect-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://github.com/Saisrikar20/DBMS) [![Views](https://komarev.com/ghpvc/?username=Saisrikar20-DBMS&label=Views&color=0e75b6&style=for-the-badge)](https://github.com/Saisrikar20/DBMS)
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
| 🟢 **Easy** | **14** | `█████████░` 93% |
| 🟡 **Medium** | **1** | `█░░░░░░░░░` 6% |
| 🔴 **Hard** | **0** | `░░░░░░░░░░` 0% |
| 🎯 **Total** | **15** | `██████████` 100% |
<!-- STATS:END -->

---

## 📑 Problem Index

The table below is **automatically generated and updated** whenever new solutions are added:

<!-- PROBLEMS_TABLE:START -->
> 💡 **Tip:** Solutions are grouped into collapsible drawers below. Click any section to expand or collapse. For the full master list, see [`SOLUTIONS.md`](./SOLUTIONS.md).

<details open>
<summary><b>🟢 Easy Problems (14)</b> — <i>Click to expand/collapse</i></summary>

| # | Problem Title | Solution | SQL Concepts / Topics |
|:---:|:---|:---:|:---|
| 196 | [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails) | [💻 SQL](./196-delete-duplicate-emails/delete-duplicate-emails.sql) | `GROUP BY` |
| 577 | [Employee Bonus](https://leetcode.com/problems/employee-bonus) | [💻 SQL](./577-employee-bonus/employee-bonus.sql) | `LEFT JOIN`, `NULL Handling` |
| 584 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee) | [💻 SQL](./584-find-customer-referee/find-customer-referee.sql) | `NULL Handling` |
| 595 | [Big Countries](https://leetcode.com/problems/big-countries) | [💻 SQL](./595-big-countries/big-countries.sql) | `Basic Filtering (WHERE)` |
| 620 | [Not Boring Movies](https://leetcode.com/problems/not-boring-movies) | [💻 SQL](./620-not-boring-movies/not-boring-movies.sql) | `ORDER BY` |
| 627 | [Swap Sex of Employees](https://leetcode.com/problems/swap-sex-of-employees) | [💻 SQL](./627-swap-sex-of-employees/swap-sex-of-employees.sql) | `CASE WHEN` |
| 1258 | [Article Views I](https://leetcode.com/problems/article-views-i) | [💻 SQL](./1258-article-views-i/article-views-i.sql) | `ORDER BY`, `DISTINCT` |
| 1670 | [Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition) | [💻 SQL](./1670-patients-with-a-condition/patients-with-a-condition.sql) | `Pattern Matching (LIKE)` |
| 1827 | [Invalid Tweets](https://leetcode.com/problems/invalid-tweets) | [💻 SQL](./1827-invalid-tweets/invalid-tweets.sql) | `Basic Filtering (WHERE)` |
| 1837 | [Daily Leads and Partners](https://leetcode.com/problems/daily-leads-and-partners) | [💻 SQL](./1837-daily-leads-and-partners/daily-leads-and-partners.sql) | `GROUP BY`, `ORDER BY`, `DISTINCT` |
| 1908 | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products) | [💻 SQL](./1908-recyclable-and-low-fat-products/recyclable-and-low-fat-products.sql) | `Basic Filtering (WHERE)` |
| 2041 | [The Latest Login in 2020](https://leetcode.com/problems/the-latest-login-in-2020) | [💻 SQL](./2041-the-latest-login-in-2020/the-latest-login-in-2020.sql) | `GROUP BY` |
| 3782 | [Find Valid Emails](https://leetcode.com/problems/find-valid-emails) | [💻 SQL](./3782-find-valid-emails/find-valid-emails.sql) | `ORDER BY`, `REGEXP` |
| 3910 | [Find Books with No Available Copies](https://leetcode.com/problems/find-books-with-no-available-copies) | [💻 SQL](./3910-find-books-with-no-available-copies/find-books-with-no-available-copies.sql) | `GROUP BY`, `HAVING`, `ORDER BY`, `NULL Handling` |

</details>

<details open>
<summary><b>🟡 Medium Problems (1)</b> — <i>Click to expand/collapse</i></summary>

| # | Problem Title | Solution | SQL Concepts / Topics |
|:---:|:---|:---:|:---|
| 1327 | [Last Person to Fit in the Bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus) | [💻 SQL](./1327-last-person-to-fit-in-the-bus/last-person-to-fit-in-the-bus.sql) | `ORDER BY`, `Aggregation` |

</details>

<details>
<summary><b>🔴 Hard Problems (0)</b> — <i>Click to expand/collapse</i></summary>

_No problems in this category yet._


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
