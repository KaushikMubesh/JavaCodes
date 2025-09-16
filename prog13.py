class Solution(object):
    def earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        mini=8789728
        for i in range(len(waterStartTime)):
            for j in range(len((landStartTime))):
                wat=0
                if waterStartTime[i]<landStartTime[j]:
                    wat=waterStartTime[i]+waterDuration[i]
                    if landStartTime[j]<=wat:
                        wat+=landStartTime[j]+landDuration[j]
                    else:
                        wat+=(landStartTime[j]-wat)+landDuration[j]
                # mini=min(wat,mini)
                elif waterStartTime[i]>=landStartTime[j]:
                    wat=landStartTime[j]+landDuration[j]
                    if waterStartTime[i]<=wat:
                        wat+=waterStartTime[i]+waterDuration[i]
                    else:
                        wat+=(waterStartTime[i]-wat)+waterDuration[i]
                mini=min(wat,mini)
        print(mini)

Solution.earliestFinishTime( [2,8],[4,1],[6],[3])