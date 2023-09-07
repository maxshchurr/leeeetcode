"""

Reverse Polish notation, also known as postfix notation, contrasts with the "infix notation" of standard arithmetic expressions in which the operator symbol appears between the operands.
RPN has the property that brackets are not required to represent the order of evaluation or grouping of the terms.
For example, the infix expression (3 × 4) + (5 × 6) becomes 3 4 × 5 6 × + in reverse Polish notation

"""


# well, this is my implementation and i strongly believe that it have cons; at least DRY wasn't followed.
def rpn_calc(equation: str) -> int or float:
    stack = []
    result = ''
    operators = ['+', '-', '*', '/', 'sqrt']
    for index, symbol in enumerate(equation.split()):
        if symbol not in operators:
            stack.append(symbol)
        else:
            match symbol:
                case '+':
                    result = float(stack[-1]) + float(stack[-2])
                    stack = stack[:-2]
                case '-':
                    result = float(stack[-1]) - float(stack[-2])
                    stack = stack[:-2]
                case '*':
                    result = float(stack[-1]) * float(stack[-2])
                    stack = stack[:-2]
                case '/':
                    result = float(stack[-1]) / float(stack[-2])
                    stack = stack[:-2]
                case'sqrt':
                    result = float(stack[-1]) ** 0.5
                    stack.pop()

            try:
                stack.append(float(result))
            except ValueError:
                stack.append(int(result))

    try:
        return float(result)
    except ValueError:
        return int(result)
