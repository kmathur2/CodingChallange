'''
    https://leetcode.com/problems/word-break/
    Use  the greedy  approach,
    keep  finding  the largest string from starting
    available in dictionary, of found extract  it
    and  keep making the recursive call
   '''
def wordBreak(s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #print(s)
        if s == "":
            return False
        longestSub = findLargest(s, wordDict)
        if longestSub == s:
            return True
        remaining = s.replace(longestSub, '')
        if longestSub == "":
            return False
        return wordBreak(remaining, wordDict)



def findLargest(sub, wordDict):
    if sub == "":
        return ""
    if sub in wordDict:
        return sub
    return findLargest(sub[:len(sub) -1 ], wordDict)

if __name__ == "__main__":
  print(wordBreak("lifeascodecodeleet", ['life','leet', 'as', 'code']))
