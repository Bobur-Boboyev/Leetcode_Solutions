class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]

        for i in strs[1:]:
            index = 0

            while index < len(prefix) and index < len(i) and prefix[index] == i[index]:
                index += 1
            
            prefix = prefix[:index]

        return prefix
