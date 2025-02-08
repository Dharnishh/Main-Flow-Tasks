def check_balanced_parentheses(s):
    stack = []
    parentheses = {'(': ')', '{': '}', '[': ']'}
    for char in s:
        if char in parentheses:
            stack.append(char)
        elif char in parentheses.values():
            if not stack or parentheses[stack.pop()] != char:
                return False
    return not stack

# Example usage
if __name__ == "__main__":
    print("Balanced Parentheses:", check_balanced_parentheses("({[]})"))