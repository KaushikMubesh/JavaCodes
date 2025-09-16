class Solution:
    def totalFruit( fruits) :
        start=0
        end=0
        dic={}
        st=0
        tot=0
        j=0
        print(fruits)
        while(end<len(fruits)):
            if len(dic)<2:
                if fruits[end] not in dic:
                    dic[fruits[end]]=1
                    tot+=1
                    end+=1
                else:
                    dic[fruits[end]]+=1
                    tot+=1
                    end+=1
            else:
                if fruits[end] in dic:
                    dic[fruits[end]]+=1
                    tot+=1
                    end+=1
                else:
                    while fruits[st] not in dic:
                        st+=1
                    tot-=dic[fruits[st]]
                    del dic[fruits[st]]
                    dic[fruits[end]]=1
                    tot+=1
            print(dic,tot)
            j=max(tot,j)
        return j
                    

                
print(Solution.totalFruit([1,0,1,4,1,4,1,2,3]))



        
