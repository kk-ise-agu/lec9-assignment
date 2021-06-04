## Problem 3: How long distance individuals have travelled? 

In this problem the aim is to calculate the "distance" in meters that the individuals have travelled according the social media posts (Euclidean distances between points). In this problem, we will need the `userid` -column an the points created in the previous problem. You will need the shapefile `Kruger_posts.shp` generated in Problem 2 as input file.

Our goal is to answer these questions based on the input data:
- What was the shortest distance travelled in meters?
- What was the mean distance travelled in meters?
- What was the maximum distance travelled in meters?

**In your code, you should first:**
 - Import required modules.
 - Read in the shapefile as a geodataframe called `data`
 - Reproject the data from WGS84 projection into `EPSG:32735` -projection which stands for UTM Zone 35S (UTM zone for South Africa) to transform the data into metric system.
 
*Store the result in a variable called `data`*!


```python
# YOUR CODE HERE 1 to read data
import geopandas as gpd
from pyproj import CRS
```

- Check the crs of the input data. If this information is missing, set it as epsg:4326 (WGS84).
- Reproject the data from WGS84 to `EPSG:32735` -projection which stands for UTM Zone 35S (UTM zone for South Africa) to transform the data into metric system. (don't create a new variable, update the existing variable `data`!)"


```python
# YOUR CODE HERE 2 to set crs
```

```python
# CODE FOR TESTING YOUR SOLUTION

# Check the data
print(data.head())
```


```python
# CODE FOR TESTING YOUR SOLUTION

# Check that the crs is correct after re-projecting (should be epsg:32735)
print(data.crs)
```

 - Group the data by userid

```python
#  YOUR CODE HERE 3 to group 
grouped=None
```


```python
# CODE FOR TESTING YOUR SOLUTION

#Check the number of groups:
assert len(grouped.groups) == data["userid"].nunique(), "Number of groups should match number of unique users!"
```

**Create LineString objects for each user connecting the points from oldest to latest:**

*Suggested steps:*
- Create an empty DataFrame called `movements`. 
- Create an empty column "geometry"
- Use a for-loop where you iterate over the grouped object. For each user's data: 
    - [sort](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html) the rows by timestamp 
    - create a LineString object based on the user's points
    - Add the LineString to the geometry column of the `movements` dataframe. You can also add the `userid` in a separate column (or use the userid as index).
- Convert `movements` into a `GeoDataFrame` (you can replace the DataFrame created in the previous steps with the GeoDataFrame). Remember to set the `geometry` column.
- Set the CRS of the ``movements`` GeoDataFrame as ``EPSG:32735`` 


```python
# YOUR CODE HERE 4 to set movements
import pandas as pd
from shapely.geometry import LineString, Point
movements=None
```


```python
# CODE FOR TESTING YOUR SOLUTION

#Check the result
print(type(movements))
print(movements.crs)
print(movements["geometry"].head())
```

**Finally:**
- Check once more the crs definition of your dataframe (should be epsg:32735, define the correct crs if this information is missing)
- Calculate the lenghts of the lines into a new column called ``distance`` in ``movements`` GeoDataFrame.


```python
# YOUR CODE HERE 5 to calculate distance
```

```python
# CODE FOR TESTING YOUR SOLUTION

#Check the output
movements.head()
```


You should now be able to print answers to the following questions: 

 - What was the shortest distance travelled in meters?
 - What was the mean distance travelled in meters?
 - What was the maximum distance travelled in meters?


```python
# YOUR CODE HERE 6 to find max, min,mean of the distance.
```

- Finally, save the movements of into a Shapefile called ``some_movements.shp``


```python
# YOUR CODE HERE 7 to save as Shapefile
```

```python
# CODE FOR TESTING YOUR SOLUTION

import os

#Check if output file exists
assert os.path.isfile(fp), "Output file does not exits."
```

That's all for this week!
