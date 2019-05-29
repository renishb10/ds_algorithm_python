#Given a sentence, reverse the whole
#Eg: This sentence is the best -> best the is sentence This

def reverse_sentence1(s):
    s = s.strip()
    return " ".join(s.split()[::-1])

def reverse_sentence2(s):
    s = s.strip()
    stack = []
    reversed = []
    for w in s.split():
        stack.append(w)

    if stack:
        for w in stack:
            reversed.append(stack.pop)

    return " ".join(reversed)

print(reverse_sentence1("This sentence is the best  "))
print(reverse_sentence2("This sentence is the best  "))