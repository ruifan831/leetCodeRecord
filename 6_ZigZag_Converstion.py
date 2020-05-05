class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        rowstring=['']*numRows
        index,next_direction=0,1
        for i in s:
            rowstring[index]+= i
            if index ==0:
                next_direction=1
            elif index == numRows-1:
                next_direction=-1
            index +=next_direction
        return "".join(rowstring)