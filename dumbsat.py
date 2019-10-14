#!/usr/bin/python3

import random

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

nv = 25
f = random_formula(nv, int(nv * 4.26))
print(f)
r = dpll(f)
if r == None:
    print("unsat")
else:
    for v in r:
        print(v.name, v.value)
