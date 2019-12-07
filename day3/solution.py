
def graph_line(coords, directions):
    current_point = (0,0)
    for d in directions:
        cur_x, cur_y = current_point
        cardinal = d[0]
        distance = int(d[1:])
        if cardinal == 'R':
            for unit in range(distance):
                position = (cur_x + 1, cur_y)
                coords.append(position)
                current_point = position
                cur_x, cur_y = current_point
        elif cardinal == 'L':
            for unit in range(distance):
                position = (cur_x - 1, cur_y)
                coords.append(position)
                current_point = position
                cur_x, cur_y = current_point
        elif cardinal == 'U':
            for unit in range(distance):
                position = (cur_x, cur_y + 1)
                coords.append(position)
                current_point = position
                cur_x, cur_y = current_point
        elif cardinal == 'D':
            for unit in range(distance):
                position = (cur_x, cur_y - 1)
                coords.append(position)
                current_point = position
                cur_x, cur_y = current_point
        else:
            raise ValueError('Invalid cardinal detected: {}'.format(cardinal))


coords1 = []
coords2 = []
directions = []
with open('input.txt') as input_file:
    for line in input_file:
        directions.append(line.split(','))

line1, line2 = directions
graph_line(coords1, line1)
graph_line(coords2, line2)

common_points = set(coords1).intersection(set(coords2))

closest_distance = None
for pt in common_points:
    manhattan_distance = abs(pt[0]) + abs(pt[1])
    if closest_distance is None or manhattan_distance < closest_distance:
        closest_distance = manhattan_distance

fewest_steps = None
for pt in common_points:
    steps = coords1.index(pt) + 1 + coords2.index(pt) + 1
    if fewest_steps is None or steps < fewest_steps:
        fewest_steps = steps

print('Part One: {}'.format(closest_distance))
print('Part Two: {}'.format(fewest_steps))
