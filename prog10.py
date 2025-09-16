from collections import Counter
class Solution:
    def groupAnagrams(nums):
        dic=Counter(nums)
        print (dic)
        tmin=98342
        tmax=-1
        for i in dic:
            tmin=min(dic[i],tmin)
            tmax=max(tmax,dic[i])
        print(tmin,tmax)
        print(len(nums)-tmax)
        if len(set(nums))==len(nums):
            return 0
        # while(len(set(nums))!=1):


            
        
print(Solution.groupAnagrams( ["eat","tea","tan","ate","nat","bat"]))