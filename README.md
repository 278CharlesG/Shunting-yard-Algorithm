
# Python Simulation in Shunting-yard-Algorithm 

This is a classic Python implementation of the **Shunting-yard Algorithm**. Invented by Edsger W. Dijkstra, this algorithm is primarily used to parse mathematical expressions specified in infix notation ("1 + 2 * 3") into postfix notation ("1 2 3 * +"), which is much easier for computers to evaluate.

##  Shunting-yard Algorithm Rules

 The algorithm strictly follows these rules:

1. **Operands**: When a number is encountered, it is immediately appended straight to the `output`.
2. **Left Parenthesis `(`**: A left parenthesis is always pushed directly onto the `stack`. It acts as a barrier for precedence comparisons.
3. **Right Parenthesis `)`**: When a right parenthesis is encountered, the program pops operators off the `stack` and appends them to the `output` one by one until a left parenthesis `(` is at the top of the stack. Finally, the matching left parenthesis is popped and discarded.
4. **Operators (`+`, `-`, `*`, `/`, `^`)**: When an operator arrives, it compares its precedence and associativity with the operator at the top of the stack:
   - While the stack is not empty, the top element is not `(`, and the stack's operator has **higher precedence**, or **equal precedence but the incoming operator is left-associative**, the operator on the stack is popped to the `output`.
   - Once the condition is no longer met, the incoming operator is pushed onto the `stack`.
5. **Final Cleanup**: After reading the entire expression, any operators remaining on the `stack` are popped and appended to the `output` in order.

##  Environment
- Python 3.x or higher

##  Usage Instructions
Run the Python script in your terminal or command line.The program will expect a standard input rule from the user:

**Numbers, operators, and parentheses must be separated by spaces, for example, " 1 + 2 * ( 2 ^ 3 ) "**

