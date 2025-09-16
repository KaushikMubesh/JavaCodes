class Solution:
    @staticmethod
    def maxValue(nums):
        ho = nums.copy()
        for i in range(len(nums)):
            left = nums[:i]
            right = nums[i+1:]
            
            val = max(left) if left else -1
            val1 = min(right) if right else float('inf')
            
            f = val > nums[i]
            f1 = val1 < nums[i]
            
            if f and not f1:
                ho[i] = val
            elif not f and f1:
                ho[i] = val1
            elif f and f1:
                ho[i] = max(val, val1)  # ✅ use max for bigger adjustment
            else:
                ho[i] = nums[i]
        
        return ho

print(Solution.maxValue([2, 1, 3]))
