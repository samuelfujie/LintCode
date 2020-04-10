class Solution:
    """
    @param numerator: a integer
    @param denominator: a integer
    @return: return a string
    """
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        
        negative = False
        if (numerator < 0 and denominator > 0) or (denominator < 0 and numerator > 0):
            negative = True
            
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        integer = 0 if numerator < denominator else numerator // denominator
        remainder = numerator % denominator
        
        if remainder == 0:
            if negative:
                return '-' + str(integer)
            else:
                return str(integer)
        
        visited = {}
        index = 0
        repeated = -1
        while len(visited) < denominator:
            value = remainder * 10 // denominator
            remainder = remainder * 10 % denominator
            
            if value == 0 and remainder == 0:
                break
            
            if (value, remainder) in visited:
                repeated = visited[(value, remainder)]
                break
            
            visited[(value, remainder)] = index
            index += 1
        
        fraction = [0] * len(visited)
        for key in visited:
            index = visited[key]
            value = key[0]
            fraction[index] = str(value)
        
        if repeated != -1:
            fraction.insert(repeated, '(')
            fraction.append(')')
        
        answer = str(integer) + '.' + ''.join(fraction)
        if negative:
            return '-' + answer
        return answer