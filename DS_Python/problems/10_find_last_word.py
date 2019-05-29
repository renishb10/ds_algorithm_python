# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

def findLengthOfLastWord1(s):
    length = 0
    s = s.strip()
    if s:
        words = list(s.split(' '))
        if len(words):
            length = len(words[len(words) - 1])
    return length

def findLengthOfLastWord2(s):
    spaceIndex = 0
    s = s.strip()
    length = 0
    if s:
        for i in range(len(s)):
            if s[i] == ' ':
                spaceIndex = i

        if spaceIndex <= 0 and len(s) > 0:
            length = len(s)
        else:
            for j in range(spaceIndex + 1, len(s)):
                length += 1

    return length

print(findLengthOfLastWord1(' day'))
print(findLengthOfLastWord2(' day'))
    