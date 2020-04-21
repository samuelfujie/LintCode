class Solution:
    """
    @param s: the expression string
    @return: the answer
    """
    def calculate(self, s):
        expression = s.replace(' ', '')
        stack = []
        number = 0
        sign = '+'

        i = 0
        while i < len(expression):
            c = expression[i]

            if c.isdigit():
                number = number * 10 + int(c)

            if c == '(':
                left = 1;
                j = i + 1
                while left > 0:
                    if expression[j] == '(':
                        left += 1
                    if expression[j] == ')':
                        left -= 1
                    j += 1
                number = self.calculate(expression[i + 1: j - 1])
                i = j - 1

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

            i += 1

        return sum(stack)
