# Module to compute the intersection point given the end points of lines generated by probabilistic Hough Transform

import numpy as np 


def cross_product(x,y):
	res = np.dot(np.matrix([[0,-x[2],x[1]],[x[2],0,-x[0]],[-x[1],x[0],0]]),np.array(y).T)
	return np.array(res)

def lines_from_points(points):
    lines = []
    # zip 결과를 리스트로 변환
    transposed_points = list(zip(*points))
    
    # 각 x 좌표와 관련된 최소 및 최대값 찾기
    left_limit = min(min(transposed_points[0]), min(transposed_points[2]))
    right_limit = max(max(transposed_points[0]), max(transposed_points[2]))
    
    print('Left limit = {0}\nRight Limit = {1}'.format(left_limit, right_limit))
    
    for x1, y1, x2, y2 in points:
        point_1 = np.array([x1, y1, 1])
        point_2 = np.array([x2, y2, 1])
        line = cross_product(point_1, point_2)
        lines.append(line)
    
    return lines


def points_from_lines(lines, state):
	intersections = []

	for line_right, line_left in lines:
		right_slope = - (line_right[0][0]/line_right[0][1])
		left_slope = - (line_left[0][0]/line_left[0][1])
		#print 'Left slope = {0}\nRight slope = {1}'.format(left_slope,right_slope)
		intersection = cross_product(line_right[0],line_left[0])
		#print 'intersection = {0}'.format(intersection)
		if intersection[0][2] != 0  and (left_slope != right_slope):
			intersection = intersection/intersection[0][2]
			intersection = np.array(intersection)
			if intersection[0][0] >= 0 and intersection[0][1] >= 0:
				intersections.append(intersection[0])

	#np.save('intersection_may_16.npy', intersections)
	if len(intersections) != 0:
		x_cordinates =  list(zip(*intersections))[0]
		y_coordinates =  list(zip(*intersections))[1]


		v_x = int(np.median(x_cordinates))
		v_y = int(np.median(y_coordinates))

	else: 
		v_x = int(state.value[0][0])
		v_y = int(state.value[1][0])

	return v_x,v_y












