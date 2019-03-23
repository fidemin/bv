import time
import numpy as np

def match(people):
    n = len(people)
    max_common = 0
    result = []

    for i in range(n):
        first = people[i]
        for j in range(i+1, n):
            dups = np.intersect1d(first, people[j], assume_unique=True) 
            if dups.size > max_common:
                max_common = dups.size
                result = []
                result.append((i, j))
            elif dups.size == max_common:
                result.append((i, j))

    return result


if __name__ == "__main__":
    n = int(input())

    people = []
    for _ in range(n):
        row = input().split()
        row = tuple(ord(c) - ord('A') for c in row)
        people.append(row)
    start = time.time()
    print(match(people))
    print("time diff: ", time.time() - start)
