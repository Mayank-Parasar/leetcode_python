"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function
to find the first bad version. You should minimize the number of calls to the API.

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
"""

class Solution(object):
    def __init__(self):
        self.badVer = 5 # set the bad version here

    def isBadVersion(self, version):
        if (version >= self.badVer):
            return True
        else:
            return False


    def firstBadVersion(self, n):
        if n <=0:
            # should not come here
            # assert(0)
            return None
        if n == 1:
            if self.isBadVersion(n):
                return n
            else:
                return None
        if (self.isBadVersion(n) == True and self.isBadVersion(n-1) == False):
            return n

        if (self.isBadVersion(round(n/2)) == True ):
            return self.firstBadVersion(round(n/2))
        elif (self.isBadVersion(round(n/2)) == False):
            return self.firstBadVersion(round (3*n / 4))
        pass


n = 12  # set value of n here
sol = Solution()
ret_val = sol.firstBadVersion(n)
print (ret_val, " is the first bad version ")