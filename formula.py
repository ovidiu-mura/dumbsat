class Var(object):
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def __str__(self):
        return self.name

class Lit(object):
    def __init__(self, var, sign):
        self.var = var
        self.sign = sign

    def sat(self):
        return self.var.value == self.sign

    def __str__(self):
        name = self.var.name
        if self.sign:
            return str(name)
        return "-" + str(name)

class Clause(object):
    def __init__(self, lits):
        self.lits = lits

    def sat(self):
        for l in self.lits:
            if l.sat():
                return True
        return False

    def unsat(self):
        for l in self.lits:
            if l.var.value == None or l.sat():
                return False
        return True

    def __str__(self):
        return " ".join([str(l) for l in self.lits]) + " 0"

class Formula(object):
    def __init__(self, vars, clauses):
        self.vars = vars
        self.clauses = clauses

    def sat(self):
        for c in self.clauses:
            if not c.sat():
                return False
        return True

    def unsat(self):
        for c in self.clauses:
            if c.unsat():
                return True
        return False

    def __str__(self):
        header = "p cnf {} {}\n".format(len(self.vars), len(self.clauses))
        clauses = "\n".join([str(c) for c in self.clauses])
        return header + clauses

def read_formula(filename):
    with open(filename, "r") as f:
        while True:
            header = next(f).strip()
            if header[0] != 'c':
                break
        hfields = header.split()
        assert len(hfields) == 4
        assert hfields[0] == 'p'
        assert hfields[1] == 'cnf'
        nvars = int(hfields[2])
        nclauses = int(hfields[3])
        vars = [Var(name + 1) for name in range(nvars)]
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
