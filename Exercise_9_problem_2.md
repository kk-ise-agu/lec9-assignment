## Problem 2: Points to map
 
In this problem we continue to learn how to turn latitude and longitude coordinates in to geometries.

**Our aim is to plot a map based on a set of longitude and latitude coordinates that are stored in a csv file.** 
The coordinates are in WGS84 decimal degrees (EPSG:4326), and the data is stored in `some_posts.csv` comma separated file in the folder `data`. First rows of the data look like this:
 
```
lat,lon,timestamp,userid
-24.980792492,31.484633302,2015-07-07 03:02,66487960
-25.499224667,31.508905612,2015-07-07 03:18,65281761
-24.342578456,30.930866066,2015-03-07 03:38,90916112
-24.85461393,31.519718439,2015-10-07 05:04,37959089
```

The data has 81379 rows and consists of locations and times of de-identified social media posts inside Kruger national park in South Africa:

| Column | Description |
|--------|-------------|
| lat | y-coordinate of the post |
| lon | x-coordinate of the post |
| timestamp | Time when the post was uploaded |
| userid | unique id for each user|

*Note: Although the data is based on real social media data, the userids and timestamps have been randomized making it impossible to link the data to the original posts.*

**First:**

- Import the needed modules
- Read the data from `data/some_posts.csv` into a Pandas dataframe called `data`
- Create an empty column called `geometry` where you will store shapely Point objects
- Insert Point objects into the column `geometry` based on the coordinate columns 

**HINTS:**

You want to create a Shapely point *on each row*, based on columns `'lon'` and `'lat'`. You can achieve this by using one of these alternative approaches:

- a `for`-loop and `iterrows()` to use the Point constructor on each row
- the [apply method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html) to apply the  Point constructor on each row. 
- a `for`-loop and a zipped object containing lon and lat (created using `zip`) and use the Point constructor on each lat, lon coordinate pair.


```python
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
# YOUR CODE HERE 1
```


```python
# CODE FOR TESTING YOUR SOLUTION

# Check the result
print("Number of rows:", len(data))
```

```python
# CODE FOR TESTING YOUR SOLUTION

# Check the result
print(data['geometry'].head())
```

**Next:**
- Convert that DataFrame into a GeoDataFrame using geopandas [GeoDataFrame constructor](https://geopandas.org/reference/geopandas.GeoDataFrame.html). See [hints](https://autogis-site.readthedocs.io/en/latest/lessons/L2/exercise-2.html#hints) for more details. 

- Update the CRS for coordinate system as WGS84 (i.e. epsg code: 4326)*

- Save the data into a Shapefile called `Kruger_posts.shp`

```python
import geopandas as gpd
from pyproj import CRS

# YOUR CODE HERE 2
# Convert DataFrame into a GeoDataFrame
```


```python
# CODE FOR TESTING YOUR SOLUTION

# Check the geodataframe head
print("Number of rows:", len(geo))
print(geo.head())
```


```python
# CODE FOR TESTING YOUR SOLUTION

# Check that the output file exists
import os
assert os.path.isfile(fp), "output shapefile does not exist"
```

**Finally:** 
- **Create a simple map of the points** using the `plot()` -funtion. 


```python
# YOUR CODE HERE 3
```



Well done! Now you can move on to Exercise_9_problem_3.
