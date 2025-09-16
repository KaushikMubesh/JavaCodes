class Solution:
    def maximumGain( s,x, y):
        def checkerx(s):
            y='ab'
            o='ba'
            if y in s or o in s:  
                return 1
            return 0
        if y>x:
            cx=0
            cy=0
            xc=1
            while(xc!=0):
                i=0
                l=[]
                while(i<len(s)-1):
                    if s[i]=='b' and s[i+1]=='a':
                        i=i+2
                        cx+=1
                    else:
                        l.append(s[i])
                        i=i+1
                if s[-2]=='b' and s[-1]=='a':
                    l.pop()
                else:
                    l.append(s[-1])
                s="".join(l)
                print(s)
                l=[]
                j=0
                while(j<len(s)-1):
                    if s[j]=='a' and s[j+1]=='b':
                        j=j+2
                        cy+=1
                    else:
                        l.append(s[j])
                        j=j+1
                if s[-2]=='a' and s[-1]=='b':
                    l.pop()
                else:
                    l.append(s[-1])
                s="".join(l)
                xc=checkerx(s)
                print(cx,cy,cx*x+cy*y)
                print(s)
            

Solution.maximumGain("cdbcbbaaabab",4,5)