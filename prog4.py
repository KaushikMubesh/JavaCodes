n=[]
dic={}
for i in nums:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
if len(dic)%k!=0:
    return False

for i in dic:
    if dic[i]>k:
        return False
return True