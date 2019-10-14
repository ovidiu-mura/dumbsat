#!/usr/bin/python3

import random

from formula import *

def random_formula(nvars, nclauses):
    vars = [Var(name + 1) for name in range(nvars)]
    clauses = []
    for _ in range(nclauses):
        clause = []
        for _ in range(3):
            v = random.choice(vars)
            s = bool(random.randrange(2))
            clause.append(Lit(v, s))
        clauses.append(Clause(clause))
    return Formula(vars, clauses)

nv = 25
f = random_formula(nv, int(nv * 4.26))
print(f)
