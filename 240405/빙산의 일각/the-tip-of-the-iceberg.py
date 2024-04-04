N = int(input())
heights = []
height_type = [0]
count = 0
max_mountain = 0

for i in range(N):
    h = int(input())
    if h not in height_type:
        height_type.append(h)
    heights.append(h)

for water in reversed(height_type):
    is_new = True
    count = 0
    for summit in heights:
        if summit > water and is_new:
            count += 1
            is_new = False
        else:
            if summit <= water:
                is_new = True
            continue
        if max_mountain < count:
            max_mountain = count
    if max_mountain > count:
        break

print(max_mountain)