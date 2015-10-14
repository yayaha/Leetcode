class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
        # Reverse first part
        self.reverse(nums, 0, n - k)
        # Reverse second part
        self.reverse(nums, n - k, n)
        # Reverse whole array
        self.reverse(nums, 0, n)
        
    # Reverse part of the array
    def reverse(self, nums, left, right):
        for i in xrange((right - left) / 2):
            tmp = nums[left + i]
            nums[left + i] = nums[right - i - 1]
            nums[right - i - 1] = tmp
        return nums