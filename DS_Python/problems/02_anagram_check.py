def check_anagram_1(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        print("Given strings are not in Equal length!")
    else:
        s1 = ''.join(sorted(s1.upper()))
        s2 = ''.join(sorted(s2.upper()))

        isAnagram = True
        for c in range(0, len(s1)):
            if s1[c] != s2[c]:
                isAnagram = False
                break

        return isAnagram

print(check_anagram_1('dog','God'))
print(check_anagram_1('clint Eastwood','old west action'))
