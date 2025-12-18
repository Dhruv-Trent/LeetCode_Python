# Problem:- 2300. Successful Pairs of Spells and Potions

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()

        res = []
        n =len(potions)
        for i in range (len(spells)):
            
            x = 0
            for j in range(len(potions)):
                if(spells[i]*potions[j]>=success):
                    res.append(n-x)
                    break
                else:
                    if x<n-1:
                        x+=1
                    else:
                        res.append(0)
                    

        return res
                    
                   







if __name__ == '__main__':
    sol = Solution()
    spells = [3,1,2]
    potions = [8,5,8]
    success = 16

    res = sol.successfulPairs(spells,potions,success)

    print(res)
