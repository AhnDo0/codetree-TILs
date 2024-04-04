N = int(input())
heights = []
height_type = []
count = 0
max_mountain = 0

for i in range(N):
    h = int(input())
    if h not in height_type:
        height_type.append(h)
    heights.append(h)

max_height = max(height_type)

for water in range(max_height):
    is_new = True
    count = 0
    for summit in heights:
        if summit > water and is_new:
            count += 1
            is_new = False
        else:
            is_new = True
        if max_mountain < count:
            max_mountain = count

print(max_mountain)