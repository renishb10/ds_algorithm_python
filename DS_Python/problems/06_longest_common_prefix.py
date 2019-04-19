from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
        prefix = ""
        count = 0
        if (len(strs) > 0):
            compare_string = strs[0]
            for i in range(len(compare_string)):
                compare_char = compare_string[i]
                is_equal = True
                for j in range(1, len(strs)):
                    curr_str = strs[j]
                    if i >= len(curr_str):
                        print('out index')
                        is_equal = False
                        break
                    elif curr_str[i] != compare_char:
                        print('not equal')
                        is_equal = False
                        break

                print(is_equal)
                if is_equal:
                    prefix += compare_char
                else:
                    break

        return prefix

print(longestCommonPrefix(["aca","cba"]))