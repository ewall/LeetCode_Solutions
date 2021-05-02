# LeetCode #41 https://leetcode.com/problems/first-missing-positive/

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        found = [True] + [False] * 300
        for n in nums:
            if 0 < n < 301:
                found[n] = True

        try:
            ans = found[1:].index(False) + 1
        except ValueError:
            ans = 301

        print(ans)

        return ans

if __name__ =='__main__':
    sol = Solution()
    assert sol.firstMissingPositive([]) == 1
    assert sol.firstMissingPositive([1, 2, 0]) == 3
    assert sol.firstMissingPositive([3, 4, -1, 1]) == 2
    assert sol.firstMissingPositive([7, 8, 9, 11, 12]) == 1
    assert sol.firstMissingPositive(list(range(1,301))) == 301