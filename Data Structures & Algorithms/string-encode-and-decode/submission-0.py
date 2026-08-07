class Solution:
    def encode(self, strs):
        newstr = ""
        for i in strs:
            newstr += f"{len(i)}#{i}"
        return str(newstr)
    def decode(self, s):
        res = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1  
            l = int(s[i:j])
            res.append(s[j+1:j+l+1])
            i = j+l+1
        return res

sol = Solution()
strs = [""]
encoded_string = sol.encode(strs)
decoded_strs = sol.decode(encoded_string)
print(decoded_strs)
