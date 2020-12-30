# Author: Harsh Kohli
# Date created: 11/29/2020

class Solution:

    def read(self, buf, n):
        calls, last = int(n / 4), n % 4
        if last > 0:
            calls = calls + 1
        else:
            last = 4

        ret = 0
        while calls > 0:
            buf4 = [''] * 4
            chars_read = read4(buf4)
            if calls == 1:
                chars_read = min(chars_read, last)

            for index in range(chars_read):
                buf[ret] = buf4[index]
                ret = ret + 1
            if chars_read < 4:
                break
            calls = calls - 1

        return ret
