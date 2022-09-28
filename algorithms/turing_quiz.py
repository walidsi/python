def isValid(s: str) -> bool:
    result = None

    stack = []

    stack.append(s[0])

    for c in s[1:]:
        stack.append(c)

        if (stack[-1] == ']' and len(stack) > 1 and stack[-2] == '[') or \
            (stack[-1] == ')' and len(stack) > 1 and stack[-2] == '(') or \
            (stack[-1] == '}' and len(stack) > 1 and stack[-2] == '{'):
            del stack[-1]
            del stack[-1]

    if stack == []:
        result = True
    else:
        result = False

    return result


if __name__ == '__main__':
    while True:
        line = input()

        if line == 'x':
            break

        if isValid(line):
            print('Valid')
        else:
            print('Invalid')
