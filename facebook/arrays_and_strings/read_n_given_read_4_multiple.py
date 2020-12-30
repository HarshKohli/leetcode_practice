# Author: Harsh Kohli
# Date created: 11/27/2020

"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution:

    def __init__(self):
        self.buf4 = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """

        prev_length = len(self.buf4)
        if prev_length >= n:
            for index in range(n):
                buf[index] = self.buf4[index]
            if n != prev_length:
                self.buf4 = self.buf4[n:]
            else:
                self.buf4 = []
            return n

        for index in range(n):
            buf[index] = self.buf4[index]
        self.buf4 = []
        rem = n - prev_length

        calls, last = int(rem / 4), rem % 4
        if last > 0:
            calls = calls + 1
        else:
            last = 4

        ret = 0
        do_reset = True
        while calls > 0:
            buf4 = [''] * 4
            chars_read = read4(buf4)
            iters = chars_read
            if calls == 1:
                iters = min(chars_read, last)

            for index in range(iters):
                buf[ret] = buf4[index]
                ret = ret + 1

            if iters != chars_read:
                self.buf4 = []
                for index in range(iters, chars_read):
                    self.buf4.append(buf4[index])
                do_reset = False

            if chars_read < 4:
                break
            calls = calls - 1

        if do_reset:
            self.buf4 = []

        return ret
