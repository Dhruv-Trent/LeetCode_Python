# Problem:- 68. Text Justification

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(words)
        
        while i < n:
            # Determine which words fit on this line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            # number of words in this line
            num_words = j - i
            line = ""
            
            # If last line or line has only one word, left-justify
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                # fully justify
                total_spaces = maxWidth - sum(len(words[k]) for k in range(i, j))
                space_between_words = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)
                
                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (space_between_words + (1 if k - i < extra_spaces else 0))
                line += words[j - 1]
            
            res.append(line)
            i = j
        
        return res
        
                  
        

if __name__ == '__main__':
    sol = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    res = sol.fullJustify(words,maxWidth)
    print(res)
