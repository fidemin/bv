import time

NUM = 10

def num_of_dups(a, b):
    return len(set(a).intersection(set(b)))


def match(people):
    n = len(people)
    for hobbies in people:
        hobbies.sort()

    people.sort()
    max_common = 0
    result = []

    for i in range(n):
        hobbies = people[i]
        this_max = 1
        last_ele = hobbies[NUM-this_max]
        for j in range(i+1, n):
            if people[j][0] > last_ele:
                break

            num = num_of_dups(hobbies, people[j])
            if num > this_max:
                this_max = num
                last_ele = hobbies[NUM-this_max]
            if num > max_common:
                max_common = num
                result = []
                result.append((i, j))
            elif num == max_common:
                result.append((i, j))

    return result


if __name__ == "__main__":
    n = int(input())

    people = []
    for _ in range(n):
        row = input().split()
        people.append(row)

    start = time.time() 
    print(match(people))
    print("time diff: ", time.time() - start)


