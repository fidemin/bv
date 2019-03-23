import time
from operator import itemgetter

def char_to_int(c):
    '''
    :param c string: A ~ Z 중에 알파벳 하나
    :return: A를 0으로 하는 알파벳의 포지션 리턴. B는 1이 될 것이다.
    :rtype: int
    '''
    return (ord(c) - ord('A'))


def count_bits(n):
    '''
    :param n : 정수
    :return: 정수를 bit로 표현 시 1의 개수를 리턴한다.
    :rtype: int
    '''
    return bin(n).count('1')


def num_of_matches(b1, b2):
    '''
    :param b1 b2 : 정수
    :return: b1, b2를 이진수로 표현 시, 1이 겹치는 개수를 리턴한다. 즉, intersection을 하여, 개수를
    센다고 보면 된다.
    :rtype: int
    '''
    inter = b1 & b2
    return count_bits(inter)

def is_break(first_letters, second_letters, max_matches):
    idx = 0
    while idx <= 9 and 10-max_matches+idx <= 9:
        if second_letters[idx] > first_letters[10-max_matches+idx]:
            return True
        elif second_letters[idx] == first_letters[10-max_matches+idx]:
            idx += 1
        else:
            return False


def match(people):
    n = len(people)

    max_matches = 1
    result = []

    # 현재 row와 다음 row만 비교해 빠르게 max_matches 유사 값을 가져온다.
    for i in range(n-1):
        first = people[i][1]
        second = people[i+1][1]

        matches = num_of_matches(first, second)

        if matches > max_matches:
            max_matches = matches

            if max_matches == 10:
                break


    for i in range(n):
        first = people[i]
        first_letters = first[0]
        first_bits = first[1]
        first_idx = first[2]
        for j in range(i+1, n):
            second = people[j]
            second_letters = second[0]

            if is_break(first_letters, second_letters, max_matches):
                break

            second_bits = second[1]
            second_idx = second[2]

            matches = num_of_matches(first_bits, second_bits)
            if matches > max_matches:
                max_matches = matches
                result = []
                result.append([first_idx, second_idx])
            elif matches == max_matches:
                result.append([first_idx, second_idx])

    return result


if __name__ == "__main__":
    start = time.time()
    n = int(input())
    people = []

    for i in range(n):
        row = input().split()
        value = 0
        for c in row:
            value |= 1 << char_to_int(c)

        # tuple을 요소로 넣은데
        # 첫번째 요소: 정렬된 취미 목록 
        # 두번째 요소: 알파벳의 유무를 비트로 저장. 가장 오른쪽이 A.
        # 셋번째 요소: index 값. 전체 정렬을 할 것이기 때문에 필요한다.
        people.append((tuple(sorted(row)), value, i+1))

    # 알파벳으로 표시된 정렬된 취미 목록을 기준으로 정렬한다.
    people.sort(key=itemgetter(0))

    result = match(people)
    print("time diff: ", time.time() - start)

    # 결과 값을 정렬한다. 필요 없는 작업이나 해를 확인하기 쉽도록 적용해 두었다.
    for pair in result:
        pair.sort()
    result.sort()


    '''
    for pair in result:
        print(pair[0], "-", pair[1])
    '''
    print(len(result))
