# Spark Interview Prep

Q: What is Spark?
A:
Distributed data processing engine

---

Q: What is lazy evaluation?
A:
Execution happens only when action is triggered

---

Q: Transformations vs Actions?
A:
- Transformations -> lazy (filter, select)
- Actions -> execute (show, collect)

---

Q: What causes shuffle?
A:
- groupBy
- join
- repartition

---

Q: How to optimize Spark?
A:
- Use caching
- Reduce shuffles
- Use broadcast joins
- Use partitioning
