# Problem:- 682. Baseball Game
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = []
        sum = 0
        for o in operations:
            if o == 'C':
                x = res.pop()
                sum -= x
            elif o == 'D':
                y =res[-1]*2
                res.append(y)
                sum += y
            elif o == '+':
                z =res[-1] + res[-2]
                res.append(z)
                sum += z
            else:
                res.append(int(o))
                sum += int(o)
        
        return sum
        
        
if __name__ == '__main__':
    sol = Solution()
    ops = ["5","2","C","D","+"]
    res = sol.calPoints(ops)
    print(res)
    
    
    
    
    
    
    
    
    
# # This was my first solution but there was no match case in old python.... 
# class Solution(object):
#     def calPoints(self, operations):
#         """
#         :type operations: List[str]
#         :rtype: int
#         """
#         res = []
#         sum = 0
#         for o in operations:
#             match o:
#                 case 'C':
#                     x = res.pop()
#                     sum -= x
#                 case 'D':
#                     y =res[-1]*2
#                     res.append(y)
#                     sum += y
#                 case '+':
#                     z =res[-1] + res[-2]
#                     res.append(z)
#                     sum += z
#                 case _:
#                     res.append(int(o))
#                     sum += int(o)
        
#         return sum