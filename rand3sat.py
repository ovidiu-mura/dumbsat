#!/usr/bin/python3

import random
import sys

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

argc = len(sys.argv)
assert argc <= 3
if argc <= 1:
    nv = 25
else:
    nv = int(sys.argv[1])
if argc >= 3:
    nc = int(sys.argv[2])
else:
    nc = int(nv * 4.26)

f = random_formula(nv, nc)
print(f)
