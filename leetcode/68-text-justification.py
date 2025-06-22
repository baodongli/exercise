class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        res = []
        start = 0
        while i < len(words):
            # total length of included words not including spaces
            cur_width = 0
            num_words = 0
            while i < len(words):
                # total length is length of words and one space in between
                if cur_width + i - start + len(words[i]) > maxWidth:
                    break
                num_words += 1
                cur_width += len(words[i])
                i += 1
        
            end = i
            if end == len(words) or num_words == 1:
                line = ' '.join(words[start:end])
                line += ' ' * (maxWidth - cur_width - (num_words - 1))
                res.append(line)
            else:
                line = words[start]
                spaces = maxWidth - cur_width
                for ti in range(start+1, end):
                    if num_words > 1:
                        spaces_bw = (spaces + num_words - 2) // (num_words - 1)
                    else:
                        spaces_bw = spaces
                    line += ' ' * spaces_bw + words[ti]
                    num_words -= 1
                    spaces -= spaces_bw
                res.append(line)
            start = end
        return res
