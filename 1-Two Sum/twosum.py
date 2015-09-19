class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i in xrange(len(nums)):
            if nums[i] in table:
                table[nums[i]].append(i+1)
            else:
                table[nums[i]] = [i+1]
        
        for x in table:
            y = target - x
            if (x == y) and (len(table[x]) > 1):
                return self.formatAns(table[x][0], table[x][1])
            elif y in table:
                return self.formatAns(table[x][0], table[target-x][0])
        return (1,1)
                
                
    def formatAns(self, index1, index2):
        if index1 < index2:
            return (index1, index2)
        else:
            return (index2, index1)