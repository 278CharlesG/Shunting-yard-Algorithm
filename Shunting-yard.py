
def precedence(op):                           # operator precedence

    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    elif op == '^':
        return 3
    return 0

def is_left_associative(op):        #to test if it is left-assoc
    return op != '^'

                                               #length = int(input().strip())            user input for length of expression
expression = input("").strip()                 #user input for expression
characters = expression.split()                  #separate each string by empty space

stack = []
output = []


for character in characters:

    if character.isdigit():               # if element is a number,add to the output list directly
        output.append(character)
    elif character == '(':                #when detecting ( ,add ( to stack
        stack.append(character)

    elif character == ')':
        while stack and stack[-1] != '(':
            output.append(stack.pop())            # when dectet ( , pop element from stack then add it to output list,repeat until only ( sign is in stack

        if stack:
            stack.pop()                   # pop out ( sign
    else:

        while (stack and stack[-1] != '(' and
               (precedence(stack[-1]) > precedence(character) or
                (precedence(stack[-1]) == precedence(character) and is_left_associative(character)))):              #pop stack top to output if higher/equal left-assoc prec (not in parens); then push current op.
            output.append(stack.pop())
        stack.append(character)

while stack:
    output.append(stack.pop())
print(' '.join(output))








