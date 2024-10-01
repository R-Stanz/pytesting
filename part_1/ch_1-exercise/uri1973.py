# URI/Beecrowd 1973

def star_trek(family_size, sheeps_by_farm):
    visited_stars = set()
    next_visit = 0

    while next_visit >= 0 \
        and next_visit < family_size \
        and sheeps_by_farm[next_visit] > 0:

            sheeps_by_farm[next_visit] -= 1
            visited_stars.add(next_visit)

            if sheeps_by_farm[next_visit] % 2 == 0:
                next_visit += 1
            else:
                next_visit -= 1

    return (len(visited_stars), sum(sheeps_by_farm))


'''
fs = int(input())
ls = input().split(' ')
ls = [int(i) for i in ls]

visits, sheeps_left = star_trek(fs, ls)
print(visits, sheeps_left)
'''
