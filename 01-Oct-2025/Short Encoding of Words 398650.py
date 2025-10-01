# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = [word[::-1] for word in words]
        words.sort()
        
        result = 0
        for i in range(len(words)):
            if i == len(words) - 1 or not words[i + 1].startswith(words[i]):
                # print(words[i + 1])
                result += len(words[i]) + 1
                
        return result