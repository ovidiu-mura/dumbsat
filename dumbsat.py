#!/usr/bin/python3

import sys

from formula import *

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

