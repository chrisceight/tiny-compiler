class Num:
    def __init__(self, v): self.v = v
class Var:
    def __init__(self, n): self.n = n
class BinOp:
    def __init__(self, l, op, r): self.l = l; self.op = op; self.r = r
class Assign:
    def __init__(self, name, expr): self.name = name; self.expr = expr
class Print:
    def __init__(self, expr): self.expr = expr
