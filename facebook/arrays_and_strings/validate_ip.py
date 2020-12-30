# Author: Harsh Kohli
# Date created: 10/21/2020

def validIPAddress(IP):
    v4, v6 = IP.split('.'), IP.split(':')
    if len(v4) == 4:
        for index, part in enumerate(v4):
            if len(part) > 3 or len(part) < 1:
                return 'Neither'
            for digit_num, digit in enumerate(part):
                if digit_num == 0 and digit == '0' and len(part) != 1:
                    return 'Neither'
                if 48 <= ord(digit) <= 57:
                    continue
                else:
                    return 'Neither'
            int_part = int(part)
            if int_part > 255:
                return 'Neither'
        return 'IPv4'
    elif len(v6) == 8:
        for index, part in enumerate(v6):
            if len(part) > 4 or len(part) < 1:
                return 'Neither'
            for digit in part:
                dig_ord = ord(digit)
                if 48 <= dig_ord <= 57 or 65 <= dig_ord <= 70 or 97 <= dig_ord <= 102:
                    continue
                else:
                    return 'Neither'
        return 'IPv6'
    else:
        return 'Neither'


IP = "172.16.254.1"
print(validIPAddress(IP))
