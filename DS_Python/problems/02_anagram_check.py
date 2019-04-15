import time

#Using Sorting and Comparing
def check_anagram_1(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        print("Given strings are not in Equal length!")
        return False
    else:
        s1 = ''.join(sorted(s1.upper()))
        s2 = ''.join(sorted(s2.upper()))

        for c in range(0, len(s1)):
            if s1[c] != s2[c]:
                return False

        return True

#Using Dictionary and Comparing
def check_anagram_2(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        print("Given strings are not in Equal length!")
        return False
    else:
        hash = {}
        for letter in s1:
            if letter in hash:
                hash[letter] += 1
            else:
                hash[letter] = 1

        for letter in s2:
            if letter in hash:
                hash[letter] -= 1
            else:
                hash[letter] = 1

        for k in hash:
            if hash[k] != 0:
                return False

        return True

print(check_anagram_1('dog','God'))
print(check_anagram_1('clint Eastwood','old west action'))

print('--------------------------------------------------')

print(check_anagram_2('dog','God'))
print(check_anagram_2('clint Eastwood','old west action'))
