from shapely.geometry import Point,LineString,Polygon
from  Exercise_1_problem_1_2 import create_line_geom,create_point_geom,create_poly_geom,get_centroid,get_area,get_length

def test_1():
	assert create_point_geom(0.0,1.1)==Point(0,1.1)

def test_2():
	assert create_line_geom([Point(45.2,22.34),Point(100.22,-3.20)]).geom_type=="LineString"
	assert create_line_geom([Point(45.2,22.34),Point(100.22,-3.20)])==LineString([Point(45.2,22.34),Point(100.22,-3.20)])

def test_3():
 	assert create_poly_geom([(45.2, 22.34),(100.22, -3.20),(70.0, 10.20)])==Polygon([(45.2, 22.34),(100.22, -3.20),(70.0, 10.20)])

def test_4():
	poly1 = Polygon([(45.2, 22.34),(100.22, -3.20),(70.0, 10.20)])
	assert get_centroid(poly1)==Polygon([(45.2, 22.34),(100.22, -3.20),(70.0, 10.20)]).centroid

def test_5():
	poly1 = Polygon([(45.2, 22.34),(100.22, -3.20),(70.0, 10.20)])
	assert round(get_area(poly1),2)==17.28

def test_6():
	poly1 = Polygon([(45.2, 22.34),(100.22, -3.20),(70.0, 10.20)])
	assert round(get_length(poly1),2)==121.33


