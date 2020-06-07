class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        digits[i] +=1
        increment_next_digit=0
        result=[]
        while i>=0: 
            digits[i] += increment_next_digit
            increment_next_digit = digits[i] // 10
            if increment_next_digit == 1:
                digits[i] =digits[i]%10
                result = [digits[i]]+result
            if increment_next_digit == 0:
                result=[digits[i]]+result
                break
            i -= 1
        if increment_next_digit == 1:
            result.insert(0,increment_next_digit)
            return result
        elif i>=0:
            return digits[:i]+result
        else:
            return result