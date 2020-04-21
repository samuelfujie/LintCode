class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        expression = s.replace(' ', '')
        stack = []
        current_sum = 0
        number = 0
        sign = 1

        for char in expression:
            if char.isdigit():
                number = number * 10 + int(char)
            if char == '+':
                current_sum += sign * number
                sign = 1
                number = 0
            if char == '-':
                current_sum += sign * number
                sign = -1
                number = 0
            if char == '(':
                stack.append(current_sum)
                stack.append(sign)
                current_sum = 0
                sign = 1
                number = 0
            if char == ')':
                current_sum += sign * number
                current_sum *= stack.pop()
                current_sum += stack.pop()
                sign = 1
                number = 0

        return number * sign + current_sum
