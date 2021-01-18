# Author: Harsh Kohli
# Date created: 1/17/2021

class Codec:
    def encode(self, strs: [str]) -> str:
        encoded = ''
        for s in strs:
            size = str(len(s))
            proceeding_zeros = 4 - len(size)
            x = ''
            for _ in range(proceeding_zeros):
                x = x + '0'
            x = x + size
            encoded = encoded + x + s
        return encoded

        # if len(strs) == 0:
        #     return None
        # return '!@#$%'.join(strs)

    def decode(self, s: str) -> [str]:
        decoded, index = [], 0
        while index < len(s):
            size = int(s[index: index + 4])
            small_s = s[index + 4: index + 4 + size]
            decoded.append(small_s)
            index = index + 4 + size

        return decoded

        # if s is None:
        #     return []
        # return s.split('!@#$%')


# strs = ['a', 'b', 'c']
strs = []
codec = Codec()
decoded = codec.decode(codec.encode(strs))
print(decoded)
