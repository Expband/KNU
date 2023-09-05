def is_point_inside_square(point, center, side_length):
    half_side = side_length / 2
    x_min, x_max = center[0] - half_side, center[0] + half_side
    y_min, y_max = center[1] - half_side, center[1] + half_side
    return (x_min <= point[0] <= x_max) and (y_min <= point[1] <= y_max)
table_1_raw = """
2,3 0,1 2,4 0,0 1,2 0,2 2,2 1,1
0,9 2,0 3,3 2,3 1,3 2,4 3,2 1,5
1,0 3,1 1,1 2,0 2,1 2,8 1,0 4,3
0,2 1,5 1,3 1,0 2,2 1,2 1,1 6,6
2,2 5,2 1,3 0,2 3,1 2,7 1,2 3,3
1,1 1,4 3,1 1,0 2,2 0,9 2,1 2,5
0,0 4,4 2,3 5,0 1,3 2,3 2,0 4,1
5,2 3,0 0,2 0,5 1,2 2,3 3,2 0,3
3,6 2,6 3,1 3,3 1,1 2,3 4,2 0,2
2,0 6,0 5,1 2,2 1,2 0,3 3,1 0,1
0,4 0,1 6,4 4,2 2,3 1,0 1,5 1,0
2,2 4,0 2,4 2,1 1,2 1,0 2,3 2,0
3,1 3,3 3,2 1,3 2,2 2,3 4,0 3,0
1,3 2,2 1,2 0,1 3,1 2,3 0,2 4,2
0,2 1,1 5,5 2,6 2,1 0,0 6,2 3,1
2,0 2,2 4,3 4,2 0,2 2,1 3,3 2,4
"""
table_2_raw = """
2,0 6,0 5,1 2,2 1,2 0,3 3,1 0,1
0,2 1,1 5,5 2,6 2,1 0,0 6,2 3,1
2,2 5,2 1,3 0,2 3,1 2,7 1,2 3,3
0,0 4,1 2,3,1 3,3 3,2 1,3 2,1 2,2 4,0 3,0
2,3 0,1 2,4 0,0 1,2 0,2 2,2 1,1
1,1 1,4 3,1 1,0 2,2 0,9 2,1 2,5
0,4 0,1 6,4 4,2 2,3 1,0 1,5 2,0
2,0 2,2 4,3 4,2 0,2 2,1 3,3 2,4
5,2 3,0 0,2 0,5 1,2 2,3 3,2 0,3
0,2 1,5 1,2 1,0 2,2 1,2 1,1 6,6
3,6 2,6 3,1 2,3 1,1 3,3 4,2 0,2
2,2 4,0 2,0 2,1 1,2 1,0 2,3 2,0
1,3 2,2 1,2 0,1 3,1 2,3 0,2 4,2
1,0 3,1 1,1 2,0 2,1 2,8 1,0 4,3
0,9 2,0 3,3 2,3 1,3 2,4 3,2 1,5
"""
table_1 = [tuple(map(int, coords.split(','))) for coords in table_1_raw.split()]
table_2 = [tuple(map(int, coords.split(','))) for coords in table_2_raw.split()]
larger_circle_center = (0, 0)
larger_circle_side = 12
smaller_circle_center = (0, 0)
smaller_circle_side = 6
points_table_1 = {'inside_larger': [], 'inside_smaller': [], 'outside': [], 'boundary': []}
points_table_2 = {'inside_larger': [], 'inside_smaller': [], 'outside': [], 'boundary': []}

for point in table_1:
    if is_point_inside_square(point, larger_circle_center, larger_circle_side):
        if is_point_inside_square(point, smaller_circle_center, smaller_circle_side):
            points_table_1['inside_smaller'].append(point)
        else:
            points_table_1['inside_larger'].append(point)
    else:
        points_table_1['outside'].append(point)

for point in table_2:
    if is_point_inside_square(point, larger_circle_center, larger_circle_side):
        if is_point_inside_square(point, smaller_circle_center, smaller_circle_side):
            points_table_2['inside_smaller'].append(point)
        else:
            points_table_2['inside_larger'].append(point)
    else:
        points_table_2['outside'].append(point)

print(points_table_1)
print(points_table_2)



