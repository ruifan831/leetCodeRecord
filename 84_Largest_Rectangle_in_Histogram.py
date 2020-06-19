class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack=[-1]
        res=0
        for i,num in enumerate(heights):
            # using stack, if current number is smaller than the last element in stack
            # pop out the last element in stack and calculate the area
            # then add the current index to the stack
            while stack[-1]!=-1 and heights[stack[-1]]>=num:
                # the rectangle that the last element of the stack can construct is
                # height = the corresponding num in the heights list for the last element in the stack
                # width = current index - the last element in the stack after the pop out -1
                index = stack.pop()
                height = heights[index]
                width = i-stack[-1]-1
                res = max(res,height*width)
            stack.append(i)
        
        return res