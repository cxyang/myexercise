# coding=utf-8

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


def main():
    s = "hello world"
    t = "world hello"

    solution = Solution()

    print(Solution().isAnagram(s, t))


if __name__ == "__main__":
    main()



