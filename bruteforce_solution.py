import time

def char_to_int(c):
    return (ord(c) - ord('A'))

def count_bits(n):
    return bin(n).count('1')


def match(people):
    n = len(people)
    max_common = 0
    result = []

    for i in range(n):
        first = people[i]
        for j in range(i+1, n):
            inter = first & people[j]
            num = count_bits(inter)
            if num > max_common:
                max_common = num
                result = []
                result.append((i+1, j+1))
            elif num == max_common:
                result.append((i+1, j+1))

    return result


if __name__ == "__main__":
    start = time.time()
    n = int(input())

    people = []
    for _ in range(n):
        row = input().split()
        value = 0
        # 알파벳에 해당하는 위치를 bit로 저장한다.
        for c in row:
            value |= 1 << char_to_int(c)
        people.append(value)
    result = match(people)
    print("time diff: ", time.time() - start)

    print("the number of results: %d" % len(result))
    for pair in result:
        print(pair[0], "-", pair[1])
