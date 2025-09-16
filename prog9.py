class Solution:
    def findRelativeRanks( score):
        dic={}
        for i in range(len(score)):
            dic[score[i]]=i
        cp=score.copy()
        cp.sort(reverse=True)
        for i in range(len(cp)):
            if i==0:
                score[dic[cp[i]]]="Gold Medal"
            elif i==1:
                score[dic[cp[i]]]="Silver Medal"
            elif i==2:
                score[dic[cp[i]]]="Bronze Medal"
            else:
                score[dic[cp[i]]]=str(i+1)
        return score
print(Solution.findRelativeRanks([1,10,8,9,4]))