class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        INT_MAX = 2 ** 31-1
        INT_MIN = -2 ** 31

        negative = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        res = self.positive_divide(dividend, divisor)
        res = res if not negative else -res

        if res > INT_MAX or res < INT_MIN:
            return INT_MAX
        return res

    def positive_divide(self, dividend, divisor):
        if (dividend < divisor):
            return 0
        sum = divisor
        multiple = 1
        while sum + sum <= dividend:
            sum *= 2
            multiple *= 2
        return multiple + self.positive_divide(dividend - sum, divisor)
