class Solution:
    def isTrionic( nums):
        if len(nums) < 5:
            return False
        def asc(l):
            if len(l)==1:
                return False
            for i in range(1,len(l)):
                if l[i]<=l[i-1]:
                    return 0
            return 1
        def decch(l):
            if len(l)==1:
                return False
            for i in range(1,len(l)):
                if l[i]>=l[i-1]:
                    return 0
            return 1
        def asc1(l):
            for i in range(1,len(l)):
                if l[i]<=l[i-1]:
                    return 0
            return 1
    
        l=[]
        l.append(0)
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                l.append(i)
                break
            if i==len(nums)-1:
                return False
        for i in range(l[1]+1,len(nums)):
            if nums[i]>nums[i-1]:
                l.append(i)
                break
            if i==len(nums)-1:
                return False
        if len(l)<3:
            return False
        print(l)
        f=nums[:l[1]]
        h=nums[l[1]:l[2]]
        k=nums[l[2]:]
        print(f,h,k)
        a1=asc(f)
        a2=decch(h)
        a3=asc1(k)
        return a1==1 and a2==1 and a3==1
        # return False
print(Solution.isTrionic([1,3,5,4,2,6]))
        
        