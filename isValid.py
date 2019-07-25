def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
            
        else:
            if (stack[-1] == "{" and s[i] == "}") \
                or (stack[-1] == "[" and s[i] == "]") \
                or (stack[-1] == "(" and s[i] == ")"):
                stack.pop()
                
            else:
                stack.append(s[i])
                
    return len(stack) == 0