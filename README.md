# "Dumb" CNF SAT Solvers
Bart Massey

This Python 3 codebase comprises three tools:

* `rand3sat.py`: Produce a random 3-CNF-SAT instance on
  standard output.

* `dumbdpll.py`: Solve a CNF-SAT instance using the
  [DPLL Algorithm](https://en.wikipedia.org/wiki/DPLL_algorithm)
  (but without unit propagation or pure literal removal).

* `dumbwsat.py`: Try to solve a satisfiable CNF-SAT instance
  using [WalkSAT](https://en.wikipedia.org/wiki/WalkSAT).

Programs input and output in
[DIMACS 2009 format](http://www.satcompetition.org/2009/format-solvers2009.html).
Please run with `--help` for program usage.

Two sample instances are supplied: one SAT and one UNSAT.
