class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        words_dict = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in words_dict:
                words_dict[key].append(s)
            else:
                words_dict[key] = [s]

        result = []
        for value in words_dict.values():
            result.append(value)

        return result