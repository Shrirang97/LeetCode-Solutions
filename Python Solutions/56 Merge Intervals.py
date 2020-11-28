'''
Link: https://leetcode.com/problems/merge-intervals/



'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervalsEnd = 0
        for interval in intervals:
            intervalsEnd = max(intervalsEnd,interval[1])
        intervalsEnd +=1
        mergeList = [0 for x in range(intervalsEnd)]
        print(mergeList,len(mergeList))
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            while start<=end:
                mergeList[start] +=1
                start +=1
        start, end, ans = -1, -1, []
        for i in range(intervalsEnd+1):
            if mergeList[i]>0:
                if start==-1:
                    start = i
                else:
                    end = i
            else:
                if end!=-1:
                    ans.append([start,end])
                    start, end = -1,-1
        return ans