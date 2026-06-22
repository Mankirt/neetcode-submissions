class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord: return 1
        wordList = set(wordList)
        if endWord not in wordList: return 0

        
        dict_map = defaultdict(list)
        length = len(beginWord)
        for word in list(wordList):
            each_word_list = list(word)
            for i in range(length):
                temp = each_word_list.copy()
                temp[i] = "*"
                dict_map[tuple(temp)].append(word)
        
        q = deque([beginWord])
        seen = set()
        seen.add(beginWord)
        ans = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return ans
                each_word_list = list(word)
                for i in range(length):
                    temp = each_word_list.copy()
                    temp[i] = "*"
                    for item in dict_map[tuple(temp)]:
                        if item not in seen:
                            q.append(item)
                            seen.add(item)
            ans += 1
        return 0
