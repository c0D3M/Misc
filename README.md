**NP**: Set of decision problems which can be verified in polynomial time.

**NP Hard**: A problem is said to be NP-Hard if it belongs to NP and all problems in NP can be reduced to it in polynomial time.

**NP Complete**: Belongs to NP as well as NP-Hard.
All NP-Complete problems are NP-Hard but all NP_Hard not equals to NP-Complete.
To prove a new problem is NP-Complete, first prove it whether it NP and then reduce any of the exisiting NP-Complete problem to it.
https://en.wikipedia.org/wiki/List_of_NP-complete_problems
Karp 21 problems: https://en.wikipedia.org/wiki/Karp%27s_21_NP-complete_problems

NP- Complete can be solved in following way

|     | polynomial time|Optimal Solution | All Cases
------|-------|------|------
Special Case (Independent Set, 2-SAT)| OK       |OK| NO
Approximate Algorithm (Vertex Cover, Metric TSP)| OK       |NO| OK
Exact Algorithm (Dynamic TSP)| NO       |OK| OK

Metric-TSP: Satisfy Triangle Inequality i.e. AB <= AC+BC
Dynamic-TSP: Held-Karp Algorithm using Dynamic Programming.
