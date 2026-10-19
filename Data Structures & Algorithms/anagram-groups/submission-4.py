class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        words_dict = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in words_dict:
                words_dict[key].append(s)
            else:
                words_dict[key] = [s]


        return list(words_dict.values())