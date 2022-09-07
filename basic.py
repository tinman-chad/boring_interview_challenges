#find the Nth value of the fibonacci sequence (for sprint story pointing purposes)
def fibonacci_value_at(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

#is it a palindrome

def is_palindrome(s):
    return str(s) == str(s)[::-1]

#merge two sorted listes
def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result