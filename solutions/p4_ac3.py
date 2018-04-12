# -*- coding: utf-8 -*-

from collections import deque
import p2_is_consistent


def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

    # TODO implement this
    while len(queue_arcs) != 0:
        xi, xj = queue_arcs.pop()
        if len(xi.domain) == 0:
            return False
        if revise(csp, xi, xj):
            if len(xi.domain) == 0:
                return False
            for xk in csp.constraints[xi]:
                tup = (xk.var2, xi)
                queue_arcs.append(tup)
    return True
    # pass


def revise(csp, xi, xj):
    removed = False
    consistent = False
    for x in xi.domain:
        for y in xj.domain:
            if p2_is_consistent.is_consistent(csp, xj, y):
                consistent = True
        if not consistent:
            xi.domain.remove(x)
            removed = True
    return removed

    pass