# -*- coding: utf-8 -*-

from collections import deque
import p2_is_consistent
import p1_is_complete
import p5_ordering
# from timeit import default_timer





def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P6, *you do not need to modify this method.*
    """
    return ac3(csp, csp.constraints[variable].arcs())


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P6, *you do not need to modify this method.*
    """
    # start = default_timer()

    if backtrack(csp):
        # print "Backtrack time: ", default_timer() - start
        return csp.assignment
    else:
        # print "Backtrack time: ", default_timer() - start
        # print "No solution!"
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """

    # TODO copy from p3

    # Checks is CSP has a solution
    if p1_is_complete.is_complete(csp):
        return True

    # Variable returned from MRV/degree heuristic
    var = p5_ordering.select_unassigned_variable(csp)

    if var is None:
        return False

    # Loop through ordered domains values using LCV heuristic
    for value in p5_ordering.order_domain_values(csp, var):

        # Save state of all variables
        csp.variables.begin_transaction()

        # Checks if the domain value is consistent
        if p2_is_consistent.is_consistent(csp, var, value):
            var.assign(value)

            # Calls AC3 and returns True/False
            inferences = inference(csp, var)
            if inferences:

                # Recursively call backtrack
                result = backtrack(csp)
                if result:
                    return True

        # Revert back to saved state
        csp.variables.rollback()
        var.domain.remove(value)

        if len(var.domain) == 0:
            return False
    return False



def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise.  Note that this method does not
    return any additional variable assignments (for simplicity)."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

    # TODO copy from p4
    while len(queue_arcs) != 0:
        xi, xj = queue_arcs.pop()
        if len(xi.domain) == 0:
            return False

        if len(xj.domain) == 0:
            return False

        if revise(csp, xi, xj):
            if len(xi.domain) == 0:
                return False

            for xk in csp.constraints[xi]:
                tup = (xk.var2, xi)
                if len(xk.var2.domain) == 0:
                    return False
                else:
                    queue_arcs.append(tup)
    return True
    # pass


def revise(csp, xi, xj):
    removed = False
    consistent = False
    if len(xi.domain) == 0:
        return False

    # Loop through all domain values in xi, xj and if not
    # consistent then remove domain value
    for x in xi.domain:
        for y in xj.domain:
            if p2_is_consistent.is_consistent(csp, xj, y):
                consistent = True
        if not consistent:
            xi.domain.remove(x)
            if len(xi.domain) == 0:
                return False
            removed = True
    return removed
    # pass