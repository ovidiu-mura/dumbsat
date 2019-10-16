#!/usr/bin/python3

# Try to solve CNF SAT problems using WalkSAT local search.

import argparse
import random
import sys

from formula import *

# Do a local search for a satisfying assignment.
# Return the sat assignment or None if step
# bound is exceeded.
def wsat(f, maxsteps=None, restart=None, noise=0.5):

    nsteps = 0
    nrun = 0
    nrestart = 0
    while True:
        # Check bound.
        if maxsteps != None and nsteps > maxsteps:
            return None

        # Check for restart.
        if restart != None and nrun >= restart:
            nrun = 0
            nrestart += 1

        # Randomly value all variables if needed.
        if nrun == 0:
            for v in f.vars:
                v.value = bool(random.randrange(2))

        # Do a noise flip if chosen, else a greedy flip.
        if random.random() < noise:
            v = random.choice(f.vars)
            v.value = not v.value
        else:
            flips = []
            minunsat = None
            for (i, v) in enumerate(f.vars):
                # Do-undo.
                v.value = not v.value
                n = f.nunsat()
                if minunsat == None or n <= minunsat:
                    flips.append((n, i))
                    minunsat = n
                v.value = not v.value
            assert minunsat != None
            flips = [i for n, i in flips if n == minunsat]
            i = random.choice(flips)
            f.vars[i].value = not f.vars[i].value

        # Return solution if found.
        if f.sat():
            print("nsteps:", nsteps, file=sys.stderr)
            if restart != None:
                print("nrestarts:", nrestarts, file=sys.stderr)
            return f.vars

        # Bump counters.
        nsteps += 1
        nrun += 1

    assert False

# Process arguments.
parser = argparse.ArgumentParser(description='Solve CNF formula via WSAT.')
parser.add_argument('--maxsteps', '-m', type=int,
                    default=None, help='maximum steps to try')
parser.add_argument('--restart', '-r', type=int,
                    default=None, help='restart interval')
parser.add_argument('--noise', '-n', type=float,
                    default=0.5, help='noise percentage')
parser.add_argument('file', type=str, help='instance file')
args = parser.parse_args()
maxsteps = args.maxsteps
restart = args.restart
noise = args.noise
filename = args.file

# Run the instance.
f = read_formula(args.file)
r = wsat(f, maxsteps=maxsteps, restart=restart, noise=noise)
if r == None:
    print("step bound exceeded", file=sys.stderr)
    exit(1)
print_soln(r)
