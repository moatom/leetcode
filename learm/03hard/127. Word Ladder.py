# https://leetcode.com/problems/word-ladder/description/?envType=problem-list-v2&envId=xo2bgr0r

from collections import deque
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        useableWords = set(wordList)
        if endWord not in useableWords: # 前提として必要
            return 0

        q = deque([(1, beginWord)])

        while q:
            l,w = q.popleft()
            for i in range(len(w)):
                for c in string.ascii_lowercase:
                    nw = w[:i] + c + w[i+1:]
                    if nw == endWord:
                        return l+1
                    if nw in useableWords:
                        useableWords.remove(nw)
                        q.append((l+1, nw))
        return 0
