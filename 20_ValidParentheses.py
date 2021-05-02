class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # shortcuts
        if (len(s) % 2) != 0 or s[0] in (')', '}', ']'):
            return False

        stack = []

        stack.append(s[0])
        for c in s[1:]:
            if len(stack) > 0 and ((stack[-1] == '(' and c == ')') or (stack[-1] == '{' and c == '}') or (stack[-1] == '[' and c == ']')):
                stack.pop()
            else:
                stack.append(c)

        return True if len(stack) == 0 else False


if __name__ == '__main__':
    sol = Solution()
    assert sol.isValid('{)}') == False
    assert sol.isValid('][') == False
    assert sol.isValid('{[()]}') == True
    assert sol.isValid("()[]{}") == True
    assert sol.isValid('{{{{{{{{{{}}}}}}}}}}') == True
