#return the nth permutation.

def nth_permutation(k, n):
    permutation = []
    unused = list(range(1, k+1))
    fact = [1]*(k+1)
    for i in range(1, k+1):
        fact[i] = i*fact[i-1]
    n -= 1
    while k > 0:
        part_length = fact[k]//k
        i = n//part_length
        permutation.append(unused[i])
        unused.pop(i)
        k -= 1
        n %= part_length
    return ''.join(map(str, permutation))