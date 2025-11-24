from lexer import tokenize
from ast import *
class Parser:
    def __init__(self, src):
        self.tokens = list(tokenize(src)); self.i = 0
    def peek(self): return self.tokens[self.i] if self.i < len(self.tokens) else (None, None)
    def eat(self, kind=None):
        t = self.peek(); self.i += 1; return t
    def parse(self):
        stmts = []
        while self.peek()[0]:
            stmts.append(self.statement())
        return stmts
    def statement(self):
        t = self.peek()
        if t[0] == 'ID' and self._lookahead(1)[0] == '=':
            name = self.eat('ID')[1]; self.eat('='); expr = self.expr(); self._opt(';'); return Assign(name, expr)
        if t[0] == 'ID' and t[1] == 'print':
            self.eat('ID'); self.eat('('); expr = self.expr(); self.eat(')'); self._opt(';'); return Print(expr)
        expr = self.expr(); self._opt(';'); return expr
    def _opt(self, tk):
        if self.peek()[0] == tk: self.eat(tk)
    def _lookahead(self, n):
        idx = self.i + n
        return self.tokens[idx] if idx < len(self.tokens) else (None, None)
    def expr(self):
        node = self.term()
        while self.peek()[0] in ('+','-'):
            op = self.eat()[0]; node = BinOp(node, op, self.term())
        return node
    def term(self):
        node = self.factor()
        while self.peek()[0] in ('*','/'):
            op = self.eat()[0]; node = BinOp(node, op, self.factor())
        return node
    def factor(self):
        t = self.peek()
        if t[0] == 'NUM': return Num(self.eat('NUM')[1])
        if t[0] == 'ID': return Var(self.eat('ID')[1])
        if t[0] == '(':
            self.eat('('); n = self.expr(); self.eat(')'); return n
        raise SyntaxError("Unexpected token " + str(t))
