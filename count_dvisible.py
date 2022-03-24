# How many numbers from A to B, inclusive, are divisible by another number K

def count_divisible(a, b, k):
    count = 0
    for i in range(a, b+1):
        if i % k == 0:
            count += 1
    return count

T = int(input())
output = []
for i in range(T):
    A, B, K = int(input()), int(input()), int(input())
    output.append(count_divisible(A, B, K))

for i in range(T):
    print("Case {}: {}".format(i+1, output[i]))