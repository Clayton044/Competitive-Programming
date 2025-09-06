# Problem:  Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/

def findTheLongestSubstring(s):
    vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
    mask = 0
    pos = {0: -1}
    max_len = 0
    for i, c in enumerate(s):
        if c in vowels:
            mask ^= 1 << vowels[c]
        if mask in pos:
            max_len = max(max_len, i - pos[mask])
        else:
            pos[mask] = i
    return max_len