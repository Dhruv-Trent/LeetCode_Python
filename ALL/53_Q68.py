# Problem:- 68. Text Justification

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        line = []
        length = 0
        i = 0
        
        while i<len(words):
            if length + len(line) + len(words[i])>maxWidth:
                extraSpaces = maxWidth - length
                spaces = extraSpaces// max(1,len(line)-1)
                remainder = extraSpaces % max(1,len(line)-1)
                
                for j in range(max(1,len(line)-1)):
                    line[j] += ' ' * spaces
                    if remainder:
                        line[j]+=" "
                        remainder-=1
                res.append("".join(line))
                
                line = []
                length = 0
                
            line.append(words[i])
            length+= len(words[i])
            i+=1
            
        lastLine = " ".join(line)
        trailSpaces = maxWidth - len(lastLine)
        res.append(lastLine+" "*trailSpaces)
                
            
            
        return res
        

if __name__ == '__main__':
    sol = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    res = sol.fullJustify(words,maxWidth)
    print(res)
