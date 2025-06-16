class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        anagrams = []

        for s in strs:
            ns = ''.join(sorted(s))
            if ns not in mp:
                mp[ns] = len(anagrams)
                anagrams.append([])
            anagrams[mp[ns]].append(s)
        return anagrams
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        mp = {}
        #charList = [chr(ord('a')+ i) for i in range(26)]
        
        for s in strs:
            freq = [0 for i in range(26)]
            for ch in s:
                i = ord(ch) - ord('a')
                freq[i] = freq[i] + 1
            key = ''
            #print(freq)
            for i, f in enumerate(freq):
                if f > 0:
                    key = key + chr(ord('a') + i) + str(f)
            #print(key)
            if key not in mp:
                mp[key] = len(anagrams) 
                anagrams.append([])
            anagrams[mp[key]].append(s)
        return anagrams
    '''
