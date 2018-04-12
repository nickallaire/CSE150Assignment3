# CSE 150 Introduction to Artificial Intelligence: Search and Reasoning Assignment 3

Project Overview: This assignment focuses on Constraint Satisfaction Problems (CSP). The CSP focused on in this assignment is X-Sudoku, which in addition to the usual Sudoku constraints, the two diagonals should also have unique numbers. I was tasked with solving 6 problems: 

1. Implement the is_complete method that returns True when all variables in the CSP have been assigned.

2. Implement the is_consistent method that returns True when the variable assignment to value is consistent, i.e. it does not violate any of the constraints associated with the given variable for the variables that have values assigned.

3. Implement the basic backtracking algorithm in the backtrack method. It is "basic" in a sense that the variable ordering, value ordering and inference heuristics are not implemented yet.

4. Implement the AC3 algorithm in the ac3 method. Depending on the arc parameter given, it should also act as the Maintaining Arc Consistency (MAC) algorithm. When the arc parameter is empty, it performs AC3 on all the arcs in the problem. If the arc parameter has a specific value, it performs AC3 only on those arcs given in the parameter.

5. Implement the variable and value ordering heuristics. For the variable heuristics, implement the minimum remaining values (MRV) heuristic using the degree heuristic as the tie-breaker. For the ordering, implement the least-constraining-value (LCV) heuristic.

6. Complete a faster backtracking search algorithm by augmenting the basic backtracking algorithm with the MAC inference and the variable and value ordering heuristics.

My code can be found under the solutions directory labeled p1-p6.
