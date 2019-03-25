#Find 3 integers, whose sum is closest to the target.
#    first thought, 
#    sort the array first, then use 3 pointers to move along the array.
#    store the closest and return it
#    no need to store the index of them

#may contain duplicate elements

#pointer i start iterate from front
#pointer l is the left pointer
# will move if sum is too small
#pointer r is the right pointer
# will move if the sum is too large
# 
# brute force way, we go through all the element,
# might have a better way but will deal with optimization later,
# for example, if the sum started to grow in another direction
# save to value and move on

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestTemp = float('inf')
        nums.sort()
        
        for p_i in range(len(nums)-2):
            if(p_i > 0 and nums[p_i] == nums[p_i-1]):
                continue
            p_r = len(nums) -1
            p_l = p_i + 1
            while(p_l < p_r):
                three_sum = nums[p_i] + nums[p_l] + nums[p_r]
                if(abs(target - three_sum) < abs(target-closestTemp)):
                        closestTemp = three_sum
                        #print("new: ", closestTemp)
                if(three_sum == target):
                    return three_sum
                elif(three_sum < target):
                    p_l+=1
                    while(p_l < p_r and nums[p_l] == nums[p_l-1]):
                        p_l+=1
                elif(three_sum > target):
                    p_r-=1
                    while(p_l < p_r and nums[p_r] == nums[p_r+1]):
                        p_r-=1
                    
        return closestTemp
                        
                
                
        