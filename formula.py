# CNF Formula descriptions. String representations are in DIMACS format.

# A variable. Typically name will be a positive integer,
# but arbitrary types convertible to str() are supported.
class Var(object):
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def __str__(self):
        return str(self.name)

# A literal.
class Lit(object):
    def __init__(self, var, sign):
        self.var = var
        self.sign = sign

    # Returns True iff the literal evaluates positively.  In
    # particular, returns False if the literal's variable
    # value is None.
    def sat(self):
        return self.var.value == self.sign

    # Returns True iff the literal evaluates negatively.  In
    # particular, returns False if the literal's variable
    # value is None.
    def unsat(self):
        if self.var.value == None or self.sat():
            return False
        return True

    def __str__(self):
        name = str(self.var)
        if self.sign:
            return name
        return "-" + name

# A clause.
class Clause(object):
    def __init__(self, lits):
        self.lits = lits

    # Returns True if some literal in the clause evaluates
    # positively.
    def sat(self):
        for l in self.lits:
            if l.sat():
                return True
        return False

    # Returns True if every literal in the clause evaluates
    # negatively.
    def unsat(self):
        for l in self.lits:
            if not l.unsat():
                return False
        return True

    def __str__(self):
        return " ".join([str(l) for l in self.lits]) + " 0"

# A formula.
class Formula(object):
    def __init__(self, vars, clauses):
        self.vars = vars
        self.clauses = clauses

    # Returns True iff every clause in the formula is sat.
    # In particular, if some clause is not yet known to be
    # sat, returns False.
    def sat(self):
        for c in self.clauses:
            if not c.sat():
                return False
        return True

    # Returns True iff some clause in the formula is unsat.
    # In particular, if no clause is known to be unsat,
    # returns False.
    def unsat(self):
        for c in self.clauses:
            if c.unsat():
                return True
        return False

    # Returns number of unsat clauses in n.
    def nunsat(self):
        n = 0
        for c in self.clauses:
            if c.unsat():
                n += 1
        return n
        

    def __str__(self):
        comment = "c dumbsat formula in DIMACS format\n"
        header = "p cnf {} {}\n".format(len(self.vars), len(self.clauses))
        clauses = "\n".join([str(c) for c in self.clauses])
        return comment + header + clauses

# Read a CNF formula from the given file in DIMACS 2009
# format.  Returns a Formula. Panics on ill-formatted input.
# http://www.satcompetition.org/2009/format-solvers2009.html
def read_formula(filename):
    with open(filename, "r") as f:
        # Strip leading comments.
        while True:
            header = next(f).strip()
            if header[0] != 'c':
                break

        # Parse header and create variables.
        hfields = header.split()
        assert len(hfields) == 4
        assert hfields[0] == 'p'
        assert hfields[1] == 'cnf'
        nvars = int(hfields[2])
        nclauses = int(hfields[3])
        vars = [Var(name + 1) for name in range(nvars)]

        # Read clauses. XXX No length-checking or
        # variable-count checking is currently performed.
        clauses = []
        for row in f:
            cvars = row.split()
            ncvars = len(cvars)
            assert int(cvars[ncvars - 1]) == 0
            clause = []
            for i in range(ncvars - 1):
                cvar = int(cvars[i])
                assert cvar != 0
                sign = cvar > 0
                cvar = abs(cvar)
                clause.append(Lit(vars[cvar - 1], sign))
            clauses.append(Clause(clause))

        return Formula(vars, clauses)


# Print a solution in DIMACS 2009 format.
# http://www.satcompetition.org/2009/format-solvers2009.html
def print_soln(soln):
    if soln == None:
        print("s UNSATISFIABLE")
    else:
        print("s SATISFIABLE")
        asgs = ["v"]
        for v in soln:
            if v.value == True:
                asgs.append(str(v))
            elif v.value == False:
                asgs.append("-" + str(v))
        asgs.append("0")
        print(" ".join(asgs))
