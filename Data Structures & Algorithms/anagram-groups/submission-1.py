class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        sorte = []
        for i, word in enumerate(strs):
            sortWord = "".join(sorted(word))
            if sortWord not in sorte:
                sorte.append(sortWord)
                groups.append([word])
            else:
                groups[sorte.index(sortWord)].append(word)
        return groups