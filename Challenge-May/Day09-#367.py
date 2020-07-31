"""
Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false
"""


# Time Limit Exceeded
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,num//2):
            if i * i == num:
                return True
        return False


class Solution1:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = left + (right - left) // 2
            t = mid * mid
            if t == num:
                return True
            if t < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

if __name__ == "__main__":
    S=Solution1()
    print(S.isPerfectSquare(16))