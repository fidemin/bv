import time

def match(people):
    n = len(people)
    max_common = 0
    result = []

    for i in range(n):
        first = people[i]
        for j in range(i+1, n):
            dups = first.intersection(people[j])
            if len(dups) > max_common:
                max_common = len(dups)
                result = []
                result.append((i, j))
            elif len(dups) == max_common:
                result.append((i, j))

    return result


if __name__ == "__main__":
    n = int(input())

    people = []
    for _ in range(n):
        row = input().split()
        #row = tuple(ord(c) - ord('A') for c in row)
        people.append(set(row))
    start = time.time()
    print(match(people))
    print("time diff: ", time.time() - start)


