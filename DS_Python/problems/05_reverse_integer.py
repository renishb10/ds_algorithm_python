def reverseInt(x):
    ab = abs(x)
    rev = 0
    while(ab != 0):
        reminder = ab % 10
        rev = rev * 10 + reminder
        ab = int(ab/10)
        
    if x > 0 and rev < 2**31:
        return rev
    elif x < 0 and rev <= 2**31:
        return -rev
    else:
        return 0

print(reverseInt(-321))