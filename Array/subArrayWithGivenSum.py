# Given an unsorted array of non negative integers, find a continuous subarray which adds to a given number.

'''
Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4
Sum of elements between indices
2 and 4 is 20 + 3 + 10 = 33

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4
Sum of elements between indices
1 and 4 is 4 + 0 + 0 + 3 = 7

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found
There is no subarray with 0 sum
'''


def subArraySum(array, n, sum):
    for i in range(n):
        current_sum = array[i]
        for j in range(i + 1, n):
            if current_sum == sum:
                print(i, j - 1)
                return
            if current_sum > sum or j == n:
                break
            current_sum = current_sum + array[j]
    print("No subarray found")
    return


array = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(array)
sum = 23

subArraySum(array, n, sum)

# Time Complexity: O(n^2) in worst case.
# Nested loop is used to traverse the array so the time complexity is O(n^2)
