def gen_node(node, out):
    from ast import Num, Var, BinOp, Assign, Print
    if isinstance(node, Num): out.append(('PUSH', node.v))
    elif isinstance(node, Var): out.append(('LOAD', node.n))
    elif isinstance(node, BinOp):
        gen_node(node.l, out); gen_node(node.r, out)
        out.append(({'+' :'ADD','-':'SUB','*':'MUL','/':'DIV'}[node.op],))
    elif isinstance(node, Assign):
        gen_node(node.expr, out); out.append(('STORE', node.name))
    elif isinstance(node, Print):
        gen_node(node.expr, out); out.append(('PRINT',))
def compile_stmts(stmts):
    out = []
    for s in stmts: gen_node(s, out)
    return out
