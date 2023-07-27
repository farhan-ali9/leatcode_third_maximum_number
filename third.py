class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=sorted(set(nums),reverse=True)
        if len(a)<3:
            return a[0]
        return a[2]
