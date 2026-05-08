# SQL Interview Prep

## Basic

Q: Difference between WHERE and HAVING?
A:
- WHERE filters before aggregation
- HAVING filters after aggregation

---

Q: INNER vs LEFT JOIN?
A:
- INNER -> only matching rows
- LEFT -> all left rows + matches

---

## Intermediate

Q: What is GROUP BY?
A:
Groups rows to apply aggregation functions like SUM, COUNT

---

Q: Find 2nd highest salary
A:
Use window function:

```sql
SELECT salary
FROM (
  SELECT salary, RANK() OVER (ORDER BY salary DESC) r
  FROM employees
) t
WHERE r = 2;
```

---

## Advanced

Q: What are window functions?
A:
Functions that operate across rows without collapsing them

Example:
`SUM(amount) OVER (PARTITION BY user_id)`
