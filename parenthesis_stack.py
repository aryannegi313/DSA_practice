class Solution:
    def isValid(self, stri):
        stack = []
        match = {'(':')', '{':'}', '[':']', ')':'(', '}':'{', ']':'['}
        
        for ch in stri:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1]!=match[ch]:
                    return False
                stack.pop()
            
        return len(stack) == 0
                
sol = Solution()

print(sol.isValid("({[]})"))
print(sol.isValid("(]"))
print(sol.isValid("(()[]{} )".replace(" ", "")))
print(sol.isValid("((({{{[[[]]]}}})))"))