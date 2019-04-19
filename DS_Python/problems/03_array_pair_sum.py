#Given an integer array, output all the unique pairs that sum up to a specific value k

#Naive solution - two for loop
def sum_up_pairs(arr, k):
    if len(arr) > 0:
        for i in range(0, len(arr)):
            if arr[i] < k:
                curr = arr[i]
                for j in range(i+1, len(arr)):
                    if arr[i] + arr[j] == k:
                        print('({0},{1})'.format(arr[i], arr[j]))

#0

#sum_up_pairs([1,3,2,2],4)
sum_up_pairs([1,3,2,8,4,3,6,7,5,4,3,5,67,8,7,5,1,1,1,1,5,6,7,8,4,73,3,1],1)