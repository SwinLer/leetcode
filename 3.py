class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=0
        b=0
        m=0
        t=s
        while b< len(s):
            if s[b] in t[:a]:
                if m<a:m=a
                if b==0:t=s[b+1:]
                else:t=s[b:]
                a=0
            b+=1
            a+=1
        if m==0 and len(s)!=0:
            return len(s)
        return m 
        
#字符串首重复时出现bug
#383
