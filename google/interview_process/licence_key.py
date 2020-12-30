# Author: Harsh Kohli
# Date created: 7/24/2020

def licenseKeyFormatting(S, K):
    reversed = ""
    n = len(S)
    for index in range(n - 1, -1, -1):
        if S[index] != '-':
            reversed = reversed + S[index]

    temp, output = "", ""
    n = len(reversed)
    for index, c in enumerate(reversed):
        temp = temp + c
        if len(temp) == K and index != n - 1:
            output = output + temp + "-"
            temp = ""

    output = output + temp
    final_output = ""
    n = len(output)
    for index in range(n - 1, -1, -1):
        final_output = final_output + output[index]
    final_output = final_output.upper()

    return final_output


S = "5F3Z-2e-9-w"
K = 4
output = licenseKeyFormatting(S, K)
print(output)
