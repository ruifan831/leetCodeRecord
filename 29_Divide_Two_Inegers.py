class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        if dividend < 0 and divisor <0 or dividend >0 and divisor >0:
            sign = 1
        else:
            sign =-1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor != 1:
            while dividend >= divisor:
                power = 0 
                while dividend >= (divisor<<(power+1)):
                    power+=1
                dividend -= divisor<<power
                result +=1<<power
        else:
            result = dividend
        if sign == 1:
            return min(2**31-1,result)
        else:
            
            return max(result*sign,-2**31)
            
        