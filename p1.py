
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i =0, j = 0
        sub_set = set()
        sub_len = 0
        for i in range(0,len(s)):
            while j < len(s):
                if s[j] not in sub_set:
                    sub_set.add(s[j])
                    sub_len = j-i+1 if sub_len < j-i+1 else sub_len
                    j = j+1
                else:
                    sub_set.remove(s[i])
                    break
        return sub_len

        