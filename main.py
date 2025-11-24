from parser import Parser
from codegen import compile_stmts
from vm import run
with open('program.tiny') as f:
    src = f.read()
stmts = Parser(src).parse()
bc = compile_stmts(stmts)
run(bc)
