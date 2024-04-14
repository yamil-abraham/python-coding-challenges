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
                return False
    return not stack

input_str = input()
print(balanced(input_str.split('"')[1]))
