import time
from operator import itemgetter

NUM = 10

def char_to_int(c):
    return (ord(c) - ord('A'))


def count_bits(n):
    return bin(n).count('1')


def num_of_matches(b1, b2):
    inter = b1 & b2
    return count_bits(inter)


def match(people):
    n = len(people)

    max_matches = 1
    first_total_match_position = 0
    result = []

    # 10개 매칭이 있는지 확인한다.
    # 10개 매칭이 있는지 확인하기 위해서는 현재 row와 다음 row만 보면 된다.
    for i in range(n-1):
        first = people[i][1]
        second = people[i+1][1]

        matches = num_of_matches(first, second)

        if matches > max_matches:
            max_matches = matches

            if max_matches == 10:
                first_total_match_position = i
                break


    if max_matches == 10:
        # 최대 매칭 값이 10개면 연속된 row에 값이 있다. 
        for i in range(first_total_match_position, n):
            first = people[i]
            first_bits = first[1]
            first_idx = first[2]
            for j in range(i+1, n):
                # i의 다음 열부터 비교를 하고, 한번이라도 같은 값이 아니면 for 구문을 벗어난다.
                second = people[j]
                second_bits = second[1]
                second_idx = second[2]
                if first_bits == second_bits:
                    result.append([first_idx, second_idx])
                    continue
                else:
                    break
    else:
        for i in range(n):
            first = people[i]
            first_letters = first[0]
            first_bits = first[1]
            first_idx = first[2]
            threshold = first_letters[10-max_matches]
            for j in range(i+1, n):
                second = people[j]
                second_letters = second[0]
                if second_letters[0] > threshold:
                    break

                second_bits = second[1]
                second_idx = second[2]

                matches = num_of_matches(first_bits, second_bits)
                if matches > max_matches:
                    max_matches = matches
                    result = []
                    result.append([first_idx, second_idx])
                    threshold = first_letters[10-max_matches]
                elif matches == max_matches:
                    result.append([first_idx, second_idx])

    # sort result for consistency result
    for pair in result:
        pair.sort()
    result.sort()

    return result


if __name__ == "__main__":
    n = int(input())

    people = []
    for i in range(n):
        row = input().split()
        value = 0
        for c in row:
            value |= 1 << char_to_int(c)
        people.append((tuple(sorted(row)), value, i+1))

    people.sort(key=itemgetter(0))


    start = time.time()
    print(match(people))
    print("time diff: ", time.time() - start)


