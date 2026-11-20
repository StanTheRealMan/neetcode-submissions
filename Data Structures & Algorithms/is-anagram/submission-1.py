class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count(word: str):
            char_list = {}
            for c in word:
                char_list[c] = char_list.get(c, 0) + 1
            return char_list

        return count(s) == count(t)