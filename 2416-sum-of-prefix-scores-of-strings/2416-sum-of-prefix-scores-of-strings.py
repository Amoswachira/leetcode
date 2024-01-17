class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {} ### Initialize a hash map for trie
        for w in words:
            cur = trie ### At the begining of each word, the pointer should point to the begining of the trie
            for c in w:
                ### Go through each letter to build the trie.
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
                ### Instead of store the end of the word in the regular trie, 
                ### we are storing the occurrences of the prefix at each letter
                if 'count' not in cur:
                    cur['count'] = 0
                cur['count'] += 1
        res = []
        ### Go through each word one more time to build the result
        for w in words:
            cur = trie ### Pointer point to the begining of the trie
            count = 0 ### Keep track the count of the occurrences of each prefix (letter) in this word
            for c in w:
                cur = cur[c]
                ### At each letter, we add the count we previously stored. 
                ### This is the number of occurrence of this prefix among all words.
                count += cur['count']
            res.append(count)
        return res