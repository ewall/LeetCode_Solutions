class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # naive reverse string
        s = str(x)[::-1]

        # handle negative
        neg = False
        if s[-1] == '-':
            s = s[:-1]
            neg = True

        # trim leading zeros
        while len(s) > 0 and s[0] == '0':
            s = s[1:]
        if len(s) == 0:
            return 0

        if len(s) > 10:
            return 0

        # there must be a prettier way to check if this is bigger than +2147483647/-2147483648
        if len(s) == 10:
            if int(s[0]) > 2:
                return 0
            if int(s[0]) == 2:
                if int(s[1]) > 1:
                    return 0
                if int(s[1]) == 1:
                    if int(s[2]) > 4:
                        return 0
                    if int(s[2]) == 4:
                        if int(s[3]) > 7:
                            return 0
                        if int(s[3]) == 7:
                            if int(s[4]) > 4:
                                return 0
                            if int(s[4]) == 4:
                                if int(s[5]) > 8:
                                    return 0
                                if int(s[5]) == 8:
                                    if int(s[6]) > 3:
                                        return 0
                                    if int(s[6]) == 3:
                                        if int(s[7]) > 6:
                                            return 0
                                        if int(s[7]) == 6:
                                            if int(s[8]) > 4:
                                                return 0
                                            if int(s[8]) == 4:
                                                if neg and int(s[9]) > 8:
                                                    return 0
                                                elif int(s[9]) > 7:
                                                    return 0

        r = int(s)
        if neg:
            r = -r

        return r


if __name__ == '__main__':
    sol = Solution()
    assert sol.reverse(123) == 321
    assert sol.reverse(1234567890) == 987654321
    assert sol.reverse(2147483647) == 0
    assert sol.reverse(-2147483648) == 0
    assert sol.reverse(0) == 0