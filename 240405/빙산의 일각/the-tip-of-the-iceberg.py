N = int(input())
heights = []
height_type = set()
count = 0
max_mountain = 0
checked = [0] * (N+2)

for i in range(N):
    h = int(input())
    heights.append(h)
    height_type.add(h)

count = 0

for water in height_type:
    is_new = True
    for summit in range(1, len(heights)+1):
        if checked[summit]:
            continue
        elif heights[summit-1] > water:
            if not checked[summit - 1] and not checked[summit+1]:
                count += 1
            elif checked[summit - 1] and checked[summit+1]:
                count -= 1
            checked[summit] = 1
    if max_mountain < count:
        max_mountain = count

print(max_mountain)