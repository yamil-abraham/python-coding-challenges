s = "({}[])"

def balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return
        else:
            return
            
    if not stack:
        print("True")
    else:
        return

balanced(s)