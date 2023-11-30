def KMPSearch(needle, haystack):
    M = len(needle)
    N = len(haystack)

    lps = [0] * M
    j = 0

    computeLPSArray(needle, M, lps)

    i = 0
    indices = []

    while (N - i) >= (M - j):
        print(f"Comparing haystack[{i}] = {haystack[i]} and needle[{j}] = {needle[j]}")
        if needle[j] == haystack[i]:
            i += 1
            j += 1

        if j == M:
            indices.append(i - j)
            j = lps[j - 1]

        elif i < N and needle[j] != haystack[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices


def computeLPSArray(needle, M, lps):
    length = 0
    lps[0] = 0
    i = 1

    while i < M:
        if needle[i] == needle[length]:
            print(f"{i}),{needle[i]}, {needle[length]}")
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
            print(needle[length-1])
        else:
            lps[i] = 0
            i += 1


haystack = "AABAACAADAABAABA"
needle = "AABA"
result = KMPSearch(needle, haystack)
print("Found pattern at indices:", result)
