class Solution:
    def fourSum(self, nums, target: int):
        nums=sorted(nums)
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            remain_nums=nums[i+1:]
            t = target - nums[i]
            temp_result = self.threeSum(remain_nums,t)
            if temp_result:
                result.extend(list(map(lambda x: [nums[i]]+x,temp_result)))
        return result
    

    def threeSum(self,nums,target):
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l= i+1
            r= len(nums)-1
            while l<r:
                temp_result = nums[i]+nums[l]+nums[r] -target
                if temp_result>0:
                    r-=1
                elif temp_result<0:
                    l+=1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l +=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return result

    # O(n^2)
    def fourSum_2(self,nums,target):
        d = dict()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum2 = nums[i]+nums[j]
                if sum2 in d:
                    d[sum2].append((i,j))
                else:
                    d[sum2] = [(i,j)]
        
        result = set()
        for key in d:
            value = target - key
            if value in d:
                list1 = d[key]
                list2 = d[value]
                for (i,j) in list1:
                    for (k,l) in list2:
                        if i!=k and i!=l and j!=k and j!=l:
                            flist = [nums[i],nums[j],nums[k],nums[l]]
                            flist.sort()
                            result.add(tuple(flist))
        return list(result)

