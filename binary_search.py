"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a
function to search target in nums.If target exists, then return its index.Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
Example
1:

Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9
exists in nums and its
index is 4
Example
2:

Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2
does
not exist in nums
so
return -1

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All
the
integers in nums
are
unique.
nums is sorted in ascending
order.
"""


class Solution(object):
    def __init__(self):
        pass

    def search(self, nums, target):
        """
                :type nums: List[int]
                :type target: int
                :rtype: int
        """
        size = len(nums)
        # print len(nums)
        if size == 0:
            return -1
        if size == 1 and nums[size/2] != target:
            return -1
        if nums[size / 2] == target:
            return size / 2
        if nums[size / 2] > target:
            ret_val = self.search(nums[0:size / 2], target)
            if (ret_val != -1):
                return 0 + ret_val
            else:
                return -1
        elif nums[size / 2] < target:
            ret_val = self.search(nums[size / 2:size], target)
            if (ret_val != -1):
                return size / 2 + ret_val
            else:
                return -1


mylist = [-1, 0, 3, 5, 9, 12]
# mylist = [-1, 0, 3, 5, 9, 12]
# mylist = [-1, 0, 5]
sol = Solution()
ret_val = sol.search(mylist, 2)
print (ret_val)
