def isValid(str):
    p_dict = {
        '}':'{',
        ')':'(',
        ']':'['
    }

    stack = []
    for c in str:
        if c in p_dict:
            top = stack.pop() if stack else '-'
            if p_dict[c] != top:
                return False
        else:
            stack.append(c)

    return not stack

print(isValid('(())'))