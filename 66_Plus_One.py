class Solution:
    # update the last element in the list before while loop
    # initialize increment_next_digit=0
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        digits[i] +=1
        increment_next_digit=0
        # update digits[i] by adding increment_next_digit
        # update increment_next_digit after digits[i] is updated
        # if digits[i] >=0, we need to keep increment next num in the list
        # else break the loop
        while i>=0:
            digits[i] += increment_next_digit
            increment_next_digit = digits[i] // 10
            if increment_next_digit == 1:
                digits[i] =digits[i]%10
            if increment_next_digit == 0:
                break
            i -= 1
        if increment_next_digit == 1:
            return [1]+digits
        else:
            return digits