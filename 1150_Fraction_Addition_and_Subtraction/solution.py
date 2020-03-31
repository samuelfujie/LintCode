class Solution:
    """
    @param expression: a string
    @return: return a string
    """
    def fractionAddition(self, expression):
        expression += "+"
        ans = "0/1"
        start = 0
        for i in range(1, len(expression)):
            if expression[i] in ["+", "-"]:
                num = expression[start:i]
                ans = self.add(ans, num)
                start = i
        return ans
    
    def add(self, a, b):
        if a == "0/1":
            return b if b[0] != '+' else b[1:]

        (an, ad), (bn, bd) = map(int, a.split("/")), map(int, b.split("/"))
        lcm = self.lcm(ad, bd)
        an, bn = an * (lcm // ad), bn * (lcm // bd)
        n = an + bn
        g = self.gcd(n, lcm)
        return str(n // g) + "/" + str(lcm // g)
    
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    
    def lcm(self, a, b):
        return abs(a * b) // self.gcd(a, b)