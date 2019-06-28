"""
Aladin and his Carpet.

There are n magical sources along the circular path numbered
form 0 to n - 1. The carpet consume units of magic equal to the
distance travelled.

For example, there are 4 units of magic: magic = [3, 2, 5, 4] and
distances dist = [2, 3, 4, 2]
If he start in magic[0] he got 3 points of magic. The distance to
the next point is 2, so 3 - dist[1] = 1 but he gets +3 when
 arriving (magic[1])
"""

magic = [3, 2, 5, 4]
dist = [2, 3, 4, 2]

initial_index = (int)(raw_input('Initial index: '))

magic = [8, 4, 1, 9]
dist = [10, 9, 3, 5]


def optimal_point(magic, dist):
    """Do the magic."""
    diff = [x - y for x, y in zip(magic, dist)]
    steps = count = 0
    start_index = -1
#    look for the first positive (or zero) value
    for index, item in enumerate(diff):
        if item >= 0:
            start_index = index
            break
    index = start_index
    magic_amount = magic[index]
    print('Initial magic: {}'.format(magic_amount))
    if start_index != -1:
        while (magic_amount >= dist[index]):
            aux = magic_amount - dist[index]
            index += 1
            if index >= len(magic):
                index = 0
            res = aux + magic[index]
            magic_amount = res
            print('New magic: {}'.format(magic_amount))
            count += 1
            steps += 1
            if steps >= len(magic):
                break
    res = -1
    if count >= len(magic):
        res = start_index
    else:
        res = -1

    result = {
        'diff': diff,
        'initial_index': res,
    }
    return result


print('Magic: {}'.format(magic))
print('Dist: {}'.format(dist))
res = optimal_point(magic, dist)
print(res)
