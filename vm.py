def run(bytecode):
    stack = []; env = {}
    for instr in bytecode:
        op = instr[0]
        if op == 'PUSH': stack.append(instr[1])
        elif op == 'LOAD': stack.append(env.get(instr[1], 0))
        elif op == 'STORE': env[instr[1]] = stack.pop()
        elif op == 'ADD': b,a = stack.pop(), stack.pop(); stack.append(a + b)
        elif op == 'SUB': b,a = stack.pop(), stack.pop(); stack.append(a - b)
        elif op == 'MUL': b,a = stack.pop(), stack.pop(); stack.append(a * b)
        elif op == 'DIV': b,a = stack.pop(), stack.pop(); stack.append(a // b)
        elif op == 'PRINT': print(stack.pop())
