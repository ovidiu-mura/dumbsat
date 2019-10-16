#!/usr/bin/python3

# Generate a random 3-SAT instance on stdout in DIMACS
# format with the given number / ratio of clauses and variables.

import argparse
import random
import sys

from formula import *

# Given a fixed number of variables and clauses, return a
# Formula chosen by uniform selection from the literal
# space.
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

# Process arguments.
parser = argparse.ArgumentParser(description='Produce random 3-CNF formula.')
parser.add_argument('--variables', '-v', type=int,
                    default=25, help='number of variables')
parser.add_argument('--clauses', '-c', type=int,
                    default=None, help='number of clauses')
parser.add_argument('--ratio', '-r', type=float,
                    default=None, help='clause-variable ratio')
args = parser.parse_args()
nv = args.variables
assert args.clauses == None or args.ratio == None
if args.clauses != None:
    nc = args.clauses
elif args.ratio != None:
    nc = int(args.ratio * nv)
else:
    nc = int(4.26 * nv)

f = random_formula(nv, nc)
print(f)
