class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        expression = s.replace(' ', '')
        stack = []
        sign = '+'
        number = 0

        for i, c in enumerate(expression):
            if c.isdigit(): 
                number = number * 10 + int(c)

            if not c.isdigit() or i == len(expression) - 1:
                if sign == '+':
                    stack.append(number)
                if sign == '-':
                    stack.append(-number)
                if sign == '*':
                    stack.append(stack.pop() * number)
                if sign == '/':
                    stack.append(int(stack.pop() / number))
                sign = c
                number = 0

        return sum(stack)
