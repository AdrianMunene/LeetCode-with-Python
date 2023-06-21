class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        duplicate = False
        
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                duplicate = True

        return duplicate
    
mylist = [1,2,3]
obj1 = Solution()
print(obj1.containsDuplicate(mylist))
            



