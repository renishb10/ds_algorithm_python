def findMissingElement(arr1, arr2):
    dict = {}

    for num in arr2:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1

    print(dict)
    for num in arr1:
        if num not in dict or dict[num] == 0:
            return num
        else:
            dict[num] -= 1
            
#using sorting and zip simulatenously
def findMissingElement2(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

print(findMissingElement2([1,2,3,4],[2,1,4]))