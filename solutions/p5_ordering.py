# -*- coding: utf-8 -*-
# from timeit import default_timer

import p1_is_complete

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
    the variable with the smallest number of values left in its available domain.  If MRV ties,
    then it picks the variable that is involved in the largest number of constraints on other
    unassigned variables.
    """

    # TODO implement this

    # Domain length of mrv
    mrv = 999

    # True if no return variable
    noRet = True

    # Check if CSP has a solution
    if p1_is_complete.is_complete(csp):
        return None

    # Loop through all variables in CSP, if not
    # assigned then apply MRV and degree heuristics
    for var in csp.variables:
        if len(var.domain) == 0:
            return None
        if not var.is_assigned():
            noRet = False
            if mrv == len(var.domain):
                if len(csp.constraints[var]) > len(csp.constraints[retVar]):
                    retVar = var
                    mrv = len(var.domain)
                else:
                    retVar = var
                    mrv = len(var.domain)
            elif len(var.domain) < mrv:
                mrv = len(var.domain)
                retVar = var
    if noRet:
        return None
    return retVar
    # pass



def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    This method implements the least-constraining-value (LCV) heuristic; that is, the value
    that rules out the fewest choices for the neighboring variables in the constraint graph
    are placed before others.
    """

    # TODO implement this

    # Holds number of constraints for each value in domain
    domVals = []

    # Number of constraints variable has
    numConstr = 0

    for value in variable.domain:
        for constraint in csp.constraints[variable]:
            if constraint.var2.domain.count(value) > 0:
                numConstr += 1
        domVals.append(numConstr)
        numConstr = 0

    # Simple sort to arrange domVal's in increasing order
    # and change corresponding variable domain in retDom
    # to reflect changes made in domVal

    # Domain of variable passed in
    retDom = variable.domain

    i = 0
    while i < len(domVals):
        j = 0
        while j < len(domVals):
            if i != j:
                if domVals[i] < domVals[j]:
                    k = domVals[i]
                    domVals[i] = domVals[j]
                    domVals[j] = k
                    l = retDom[i]
                    retDom[i] = retDom[j]
                    retDom[j] = l
            j += 1
        i += 1

    return retDom
    # pass
