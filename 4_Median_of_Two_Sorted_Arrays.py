class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1,len2=len(nums1),len(nums2)
        if len1>len2:
            nums1,nums2,len1,len2= nums2,nums1,len2,len1
        halfLen = (len1+len2+1)//2
        range_min,range_max=0,len1
        while range_min<=range_max:
            # i is the index of first element for right side of nums1
            i=(range_max+range_min)//2
            # j is the index of the first element for right side of nums2
            j=halfLen-i
        
            x_left= float("-inf") if i==0 else nums1[i-1]
            x_right=float("inf") if i==len1 else nums1[i]
            y_left = float("-inf") if j==0 else nums2[j-1]
            y_right = float("inf") if j==len2 else nums2[j]
            if x_left>y_right:
                range_max -=1
            elif x_right<y_left:
                range_min+=1
            else:
                if (len1+len2)%2 == 0:
                    return (max(x_left,y_left)+min(x_right,y_right))/2
                else:
                    return max(x_left,y_left)