#!/usr/bin/python3

import sys

from formula import *

def random_formula(nvars, nclauses):
    vars = [Var("A" + str(name)) for name in range(nvars)]
    clauses = []
    for _ in range(nclauses):
        clause = []
        for _ in range(3):
            v = random.choice(vars)
            s = bool(random.randrange(2))
            clause.append(Lit(v, s))
        clauses.append(Clause(clause))
    return Formula(vars, clauses)


def dpll(f):
    for v in f.vars:
        if v.value == None:
            for value in [True, False]:
                v.value = value
                if not f.unsat():
                    r = dpll(f)
                    if r != None:
                        return r
            v.value = None
            return None
    if f.sat():
        return f.vars
    return None

f = read_formula(sys.argv[1])
r = dpll(f)
if r == None:
    print("UNSAT")
else:
    print("SAT")
    asgs = []
    for v in r:
        if v.value:
            asgs.append(str(v.name))
        else:
            asgs.append("-" + str(v.name))
    asgs.append("0")
    print(" ".join(asgs))

