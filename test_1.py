from Exercise_9_problem_1_ans import func1,func2,func3,func4
from Exercise_9_problem_2_ans import func5,func6
from Exercise_9_problem_3_ans import func7,func8,func9,func10,func11


from shapely.geometry import Polygon
import geopandas as gpd
def test_1():
    assert func1()==52
def test_2():
    assert func2()=='Polygon'
def test_3():
    assert type(func3()['geometry'])==gpd.GeoSeries
def test_4():
    assert len(func4())==1
def test_5():
    assert len(func5())==81379
def test_6():
    assert type(func6())==gpd.GeoDataFrame
#def test_7():
#    assert len(func7())==2
#def test_8():
#    assert type(func8())==str
#def test_9():
#    assert func9().crs==32695
#def test_10():
#    assert movements['distance']==10
#
