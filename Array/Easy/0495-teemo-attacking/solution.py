# 495. Teemo Attacking
# https://leetcode.com/problems/teemo-attacking/

class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        totalTime=0
        for i in range(0,len(timeSeries)):
            time=timeSeries[i]+duration-1
            if(i+1<len(timeSeries) and time>=timeSeries[i+1]):
                totalTime+=timeSeries[i+1]-timeSeries[i]
            else:
                totalTime+=time-timeSeries[i]+1
        return totalTime            
            
        
