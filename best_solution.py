import time
from operator import itemgetter

NUM = 10

def char_to_int(c):
    return (ord(c) - ord('A'))

def count_bits(n):
    return bin(n).count('1')

def num_of_dups(a, b):
    return len(set(a).intersection(set(b)))


def match(people):
    n = len(people)

    max_common = 1
    result = []

    for i in range(n):
        first = people[i]
        first_bit = first[1]
        first_original = first[0]
        first_i = first[2]
        last_ele = first_original[NUM-max_common]
        for j in range(i+1, n):
            second = people[j]
            second_original = second[0]
            second_bit = second[1]
            second_i = second[2]
            if second_original[0] > last_ele:
                break

            inter = first_bit & second_bit
            num = count_bits(inter)
            if num > max_common:
                max_common = num
                result = []
                result.append((first_i, second_i))
                last_ele = first_original[NUM-max_common]
            elif num == max_common:
                result.append((first_i, second_i))

    return result


if __name__ == "__main__":
    n = int(input())

    people = []
    for i in range(n):
        row = input().split()
        value = 0
        for c in row:
            value |= 1 << char_to_int(c)
        people.append((tuple(sorted(row)), value, i))

    people.sort(key=itemgetter(0))


    start = time.time()
    print(match(people))
    print("time diff: ", time.time() - start)


