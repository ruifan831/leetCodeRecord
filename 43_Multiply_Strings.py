class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = [0]*(len(num1)+len(num2))
        # Iterate both strings from back to front,
        # Each time do multiplication only one digit for each string. The product is position at the index i+j and i+j+1 of the final string.
        for i in range(len(num1))[::-1]:
            for j in range(len(num2))[::-1]:

                temp = (ord(num1[i])-ord("0"))*(ord(num2[j])-ord("0"))
                p1,p2 = i+j,i+j+1
                newSum = result[p2]+temp
                result[p1] += newSum//10
                result[p2] = newSum%10
        resultString = ""
        for i in result:
            if i == 0 and not resultString:
                continue
            else:
                resultString+=str(i)
        if resultString:
            return resultString
        else:
            return "0"