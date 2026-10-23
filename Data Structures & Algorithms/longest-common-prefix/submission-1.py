class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])): # 0 1 2 3 and so on 
            for s in strs:# bat bag bank band
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
                    

                    



        