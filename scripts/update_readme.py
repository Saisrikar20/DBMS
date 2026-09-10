#!/usr/bin/env python3
"""
update_readme.py
Automatically scans the repository for LeetCode SQL solutions,
extracts problem metadata, computes statistics, updates README.md with
clean collapsible sections (scalable for 100+ questions), and maintains SOLUTIONS.md.
"""

import os
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"
SOLUTIONS_PATH = REPO_ROOT / "SOLUTIONS.md"

LEETCODE_PROFILE_URL = "https://leetcode.com/u/rTP0FaRcOa/"
LEETCODE_USERNAME = "rTP0FaRcOa"

IGNORED_DIRS = {".git", ".github", "scripts", ".idea", ".vscode", "__pycache__"}

DIFFICULTY_COLORS = {
    "Easy": "brightgreen",
    "Medium": "orange",
    "Hard": "red"
}

DIFFICULTY_ICONS = {
    "Easy": "🟢",
    "Medium": "🟡",
    "Hard": "🔴"
}


def detect_sql_topics(sql_content: str) -> list:
    """Analyze SQL query content to detect key topics and operations."""
    topics = []
    upper_sql = sql_content.upper()

    if "LEFT JOIN" in upper_sql:
        topics.append("`LEFT JOIN`")
    elif "RIGHT JOIN" in upper_sql:
        topics.append("`RIGHT JOIN`")
    elif "INNER JOIN" in upper_sql or " JOIN " in upper_sql:
        topics.append("`INNER JOIN`")

    if "GROUP BY" in upper_sql:
        topics.append("`GROUP BY`")
    if "HAVING" in upper_sql:
        topics.append("`HAVING`")
    if "ORDER BY" in upper_sql:
        topics.append("`ORDER BY`")
    if "DISTINCT" in upper_sql:
        topics.append("`DISTINCT`")
    if "REGEXP" in upper_sql:
        topics.append("`REGEXP`")
    elif "LIKE" in upper_sql:
        topics.append("`Pattern Matching (LIKE)`")
    if "IS NULL" in upper_sql or "IS NOT NULL" in upper_sql or "IFNULL" in upper_sql or "COALESCE" in upper_sql:
        topics.append("`NULL Handling`")
    if "OVER (" in upper_sql or "OVER(" in upper_sql or "DENSE_RANK" in upper_sql or "ROW_NUMBER" in upper_sql or "RANK()" in upper_sql:
        topics.append("`Window Functions`")
    if "CASE" in upper_sql and "WHEN" in upper_sql:
        topics.append("`CASE WHEN`")
    if "UNION" in upper_sql:
        topics.append("`UNION`")
    if "COUNT(" in upper_sql or "SUM(" in upper_sql or "AVG(" in upper_sql or "MAX(" in upper_sql or "MIN(" in upper_sql:
        if "`GROUP BY`" not in topics:
            topics.append("`Aggregation`")

    if not topics:
        topics.append("`Basic Filtering (WHERE)`")

    return topics


def scan_problems():
    """Scan the repository for problem folders containing .sql solutions."""
    problems = []

    for entry in REPO_ROOT.iterdir():
        if entry.is_dir() and entry.name not in IGNORED_DIRS and not entry.name.startswith('.'):
            sql_files = list(entry.glob("*.sql"))
            if not sql_files:
                continue

            sql_file = sql_files[0]
            sql_content = ""
            try:
                sql_content = sql_file.read_text(encoding="utf-8")
            except Exception:
                pass

            topics = detect_sql_topics(sql_content)

            dir_name = entry.name
            id_match = re.match(r"^(\d+)-(.*)$", dir_name)
            if id_match:
                problem_id = int(id_match.group(1))
                fallback_title = id_match.group(2).replace("-", " ").title()
            else:
                problem_id = 999999
                fallback_title = dir_name.replace("-", " ").title()

            title = fallback_title
            url = f"https://leetcode.com/problems/{dir_name.split('-', 1)[-1]}/"
            difficulty = "Easy"

            prob_readme = entry / "README.md"
            if prob_readme.exists():
                try:
                    content = prob_readme.read_text(encoding="utf-8")
                    title_match = re.search(r'<h2><a href="([^"]+)">([^<]+)</a></h2>', content)
                    if title_match:
                        url = title_match.group(1)
                        title = title_match.group(2).strip()

                    diff_match = re.search(r'Difficulty-(Easy|Medium|Hard)', content, re.IGNORECASE)
                    if diff_match:
                        difficulty = diff_match.group(1).capitalize()
                except Exception:
                    pass

            problems.append({
                "id": problem_id,
                "title": title,
                "difficulty": difficulty,
                "url": url,
                "dir_name": dir_name,
                "sql_filename": sql_file.name,
                "sql_rel_path": f"./{dir_name}/{sql_file.name}",
                "topics": ", ".join(topics)
            })

    problems.sort(key=lambda x: x["id"])
    return problems


def generate_badges(total: int, easy: int, medium: int, hard: int) -> str:
    """Generate dynamic shield badges for statistics."""
    lines = [
        f"[![LeetCode Profile](https://img.shields.io/badge/LeetCode-{LEETCODE_USERNAME}-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)]({LEETCODE_PROFILE_URL})",
        f"[![Solved](https://img.shields.io/badge/Solved-{total}-2563EB?style=for-the-badge&logo=leetcode&logoColor=white)]({LEETCODE_PROFILE_URL})",
        f"[![Easy](https://img.shields.io/badge/Easy-{easy}-22C55E?style=for-the-badge)]({LEETCODE_PROFILE_URL})",
        f"[![Medium](https://img.shields.io/badge/Medium-{medium}-F59E0B?style=for-the-badge)]({LEETCODE_PROFILE_URL})",
        f"[![Hard](https://img.shields.io/badge/Hard-{hard}-EF4444?style=for-the-badge)]({LEETCODE_PROFILE_URL})",
        f"[![Database](https://img.shields.io/badge/Dialect-MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://github.com/Saisrikar20/DBMS)",
        f"[![Views](https://komarev.com/ghpvc/?username=Saisrikar20-DBMS&label=Views&color=0e75b6&style=for-the-badge)](https://github.com/Saisrikar20/DBMS)"
    ]
    return " ".join(lines)


def generate_stats_table(total: int, easy: int, medium: int, hard: int) -> str:
    """Generate a clean markdown summary table with visual progress indicators."""
    def progress_bar(count, total_count):
        if total_count == 0:
            pct = 0
        else:
            pct = int((count / total_count) * 100)
        filled = int(round(pct / 10))
        bar = "█" * filled + "░" * (10 - filled)
        return f"`{bar}` {pct}%"

    easy_bar = progress_bar(easy, total)
    med_bar = progress_bar(medium, total)
    hard_bar = progress_bar(hard, total)

    table = [
        "| Difficulty | Solved | Share of Solutions |",
        "|:---|:---:|:---|",
        f"| {DIFFICULTY_ICONS['Easy']} **Easy** | **{easy}** | {easy_bar} |",
        f"| {DIFFICULTY_ICONS['Medium']} **Medium** | **{medium}** | {med_bar} |",
        f"| {DIFFICULTY_ICONS['Hard']} **Hard** | **{hard}** | {hard_bar} |",
        f"| 🎯 **Total** | **{total}** | `██████████` 100% |"
    ]
    return "\n".join(table)


def build_table_rows(problem_subset: list) -> str:
    """Helper to build a markdown table for a given list of problems."""
    if not problem_subset:
        return "_No problems in this category yet._\n"

    lines = [
        "| # | Problem Title | Solution | SQL Concepts / Topics |",
        "|:---:|:---|:---:|:---|"
    ]
    for p in problem_subset:
        lines.append(f"| {p['id']} | [{p['title']}]({p['url']}) | [💻 SQL]({p['sql_rel_path']}) | {p['topics']} |")
    return "\n".join(lines)


def generate_collapsible_problems_index(problems: list) -> str:
    """Generate collapsible accordion sections for Easy, Medium, and Hard."""
    easy_probs = [p for p in problems if p["difficulty"] == "Easy"]
    med_probs = [p for p in problems if p["difficulty"] == "Medium"]
    hard_probs = [p for p in problems if p["difficulty"] == "Hard"]

    easy_table = build_table_rows(easy_probs)
    med_table = build_table_rows(med_probs)
    hard_table = build_table_rows(hard_probs)

    easy_open = " open" if easy_probs else ""
    med_open = " open" if med_probs else ""
    hard_open = " open" if hard_probs else ""

    sections = [
        "> 💡 **Tip:** Solutions are grouped into collapsible drawers below. Click any section to expand or collapse. For the full master list, see [`SOLUTIONS.md`](./SOLUTIONS.md).\n",
        f"<details{easy_open}>",
        f"<summary><b>🟢 Easy Problems ({len(easy_probs)})</b> — <i>Click to expand/collapse</i></summary>\n",
        easy_table,
        "\n</details>\n",
        f"<details{med_open}>",
        f"<summary><b>🟡 Medium Problems ({len(med_probs)})</b> — <i>Click to expand/collapse</i></summary>\n",
        med_table,
        "\n</details>\n",
        f"<details{hard_open}>",
        f"<summary><b>🔴 Hard Problems ({len(hard_probs)})</b> — <i>Click to expand/collapse</i></summary>\n",
        hard_table,
        "\n</details>"
    ]
    return "\n".join(sections)


def generate_solutions_md(problems: list, total: int, easy: int, medium: int, hard: int):
    """Generate a dedicated comprehensive SOLUTIONS.md catalog."""
    lines = [
        "# 📑 Complete SQL Solutions Catalog",
        "",
        f"This catalog lists all **{total}** LeetCode SQL practice solutions synced from LeetCode profile [**@{LEETCODE_USERNAME}**]({LEETCODE_PROFILE_URL}).",
        "",
        f"- **Easy:** {easy} | **Medium:** {medium} | **Hard:** {hard}",
        "",
        "[⬅️ Return to README](./README.md)",
        "",
        "---",
        "",
        "| # | Problem Title | Solution | Difficulty | SQL Concepts / Topics |",
        "|:---:|:---|:---:|:---:|:---|"
    ]

    for p in problems:
        badge_color = DIFFICULTY_COLORS.get(p["difficulty"], "lightgrey")
        diff_badge = f'<img src="https://img.shields.io/badge/-{p["difficulty"]}-{badge_color}?style=flat-square" alt="{p["difficulty"]}">'
        lines.append(f"| {p['id']} | [{p['title']}]({p['url']}) | [💻 SQL]({p['sql_rel_path']}) | {diff_badge} | {p['topics']} |")

    lines.append("")
    lines.append("---")
    lines.append(f"<sub>Auto-generated by `scripts/update_readme.py` • Synced from LeetCode: [{LEETCODE_USERNAME}]({LEETCODE_PROFILE_URL})</sub>")
    
    SOLUTIONS_PATH.write_text("\n".join(lines), encoding="utf-8")


def update_readme():
    """Parse problems, format Markdown, and update README.md and SOLUTIONS.md."""
    problems = scan_problems()
    total = len(problems)
    easy = sum(1 for p in problems if p["difficulty"] == "Easy")
    medium = sum(1 for p in problems if p["difficulty"] == "Medium")
    hard = sum(1 for p in problems if p["difficulty"] == "Hard")

    badges_md = generate_badges(total, easy, medium, hard)
    stats_md = generate_stats_table(total, easy, medium, hard)
    problems_md = generate_collapsible_problems_index(problems)

    generate_solutions_md(problems, total, easy, medium, hard)

    if not README_PATH.exists():
        print(f"Error: {README_PATH} does not exist.")
        return

    content = README_PATH.read_text(encoding="utf-8")

    # Replace badges block
    if "<!-- BADGES:START -->" in content and "<!-- BADGES:END -->" in content:
        content = re.sub(
            r"<!-- BADGES:START -->.*?<!-- BADGES:END -->",
            f"<!-- BADGES:START -->\n{badges_md}\n<!-- BADGES:END -->",
            content,
            flags=re.DOTALL
        )

    # Replace stats block
    if "<!-- STATS:START -->" in content and "<!-- STATS:END -->" in content:
        content = re.sub(
            r"<!-- STATS:START -->.*?<!-- STATS:END -->",
            f"<!-- STATS:START -->\n{stats_md}\n<!-- STATS:END -->",
            content,
            flags=re.DOTALL
        )

    # Replace problems table block
    if "<!-- PROBLEMS_TABLE:START -->" in content and "<!-- PROBLEMS_TABLE:END -->" in content:
        content = re.sub(
            r"<!-- PROBLEMS_TABLE:START -->.*?<!-- PROBLEMS_TABLE:END -->",
            f"<!-- PROBLEMS_TABLE:START -->\n{problems_md}\n<!-- PROBLEMS_TABLE:END -->",
            content,
            flags=re.DOTALL
        )

    README_PATH.write_text(content, encoding="utf-8")
    print(f"Successfully updated README.md and SOLUTIONS.md: {total} total problems (Easy: {easy}, Medium: {medium}, Hard: {hard})")


if __name__ == "__main__":
    update_readme()
