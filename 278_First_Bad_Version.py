# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
import math
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first_version = 1
        last_version = n
        while (first_version <= last_version):
            middle_version = int(math.ceil(first_version+(last_version - first_version)/2))
            if isBadVersion(middle_version) == True:
                last_version = middle_version - 1
            else:
                first_version = middle_version + 1
        return first_version