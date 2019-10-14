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
            return name
        return "-" + name

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
        return " ".join([str(l) for l in self.lits])

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
        return "\n".join([str(c) for c in self.clauses])
