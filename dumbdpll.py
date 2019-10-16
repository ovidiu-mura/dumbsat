#!/usr/bin/python3

# Solve CNF SAT problems using DPLL complete search.

import sys

from formula import *

# Do a complete search for a satisfying assignment.
# Return the sat assignment or None if unsat.
def dpll(f):
    # Try valuing the next unvalued variable.
    for v in f.vars:
        if v.value == None:
            # Value each way.
            for value in [True, False]:
                v.value = value
                if not f.unsat():
                    r = dpll(f)
                    if r != None:
                        return r
            v.value = None
            return None

    # All variables have been valued. Check to see if it's a
    # solution.
    if f.sat():
        return f.vars
    return None

# Run the instance.
f = read_formula(sys.argv[1])
r = dpll(f)
print_soln(r)
