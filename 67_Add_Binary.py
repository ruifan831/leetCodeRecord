class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # convert string to int and sum together
        int_result = self.convert_to_int(a)+self.convert_to_int(b)
        if int_result:
            # convert int to string bit
            return self.convert_to_string(int_result)
        else:
            return "0"
    
    def convert_to_int(self,s):
        num=0
        i=len(s)-1
        for index,char in enumerate(s):
            if char == "1":
                num += 2**(i-index)
        return num

    def convert_to_string(self,num):
        s=""
        # keep divide num by 2
        # if current num is indivisible by 2 then we know the current bit is 1.
        while num>0:
            temp_s="0"
            if num%2 == 1:
                num-=1
                temp_s="1"
            s= temp_s+s
            num= num//2
        return s
        
            
            
            
            
        