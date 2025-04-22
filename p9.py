class Solution:
    def longestPalindrome(self, s: str) -> str:
        flg = [[False for _ in range(len(s))] for _ in range(len(s))]
        dt = 0
        max_sub = ""
        
        for dt in range(len(s)):
            for i in range(len(s)):
                if i+dt < len(s):
                    if dt == 0:
                        flg[i][i] = True
                        max_sub = s[i:i+1]
                    elif dt == 1:
                        if s[i]==s[i+1]:
                            flg[i][i+1] = True
                            max_sub = s[i:i+2]
                    else:
                        if flg[i+1][i+dt-1] and s[i]==s[i+dt]:
                            flg[i][i+dt] = True
                            max_sub = s[i:i+dt+1]
                else:
                    break
        return max_sub
        

s = Solution()
a = "aacabdkacaa"
s.longestPalindrome(a)