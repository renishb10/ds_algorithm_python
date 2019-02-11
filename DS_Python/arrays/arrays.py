numbers = [10, 20, 30, 40, 50]

#Array elements in python need not to be of same data type
print("#Array elements in python need not to be of same data type")
numbers[1] = 'Ren'

#For in loop - similar to ForEach
print("#For in loop - similar to ForEach")
for num in numbers:
    print(num)

#For loop - similar to normal for i loop
print("#For loop - similar to normal for i loop")
for i in range(len(numbers)):
    print(numbers[i])

#Simple ranging in python
print("#Simple ranging in python")
print("#numbers[startIndex : lastIndex")
print("#It excludes last index and prints the before element till the start index")
print(numbers[3:5])

print('#Excluding last index')
print(numbers[:-1])

print('#Print the maximum value in the array O(N)')
numbers[1] = 300
max = numbers[0]
for num in numbers:
    if (num > max):
        max = num
print(max)