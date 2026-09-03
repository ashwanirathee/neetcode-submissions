class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for i in string:
                count[ord(i) - ord('a')] += 1
            freq_map[tuple(count)].append(string)
        return list(freq_map.values())