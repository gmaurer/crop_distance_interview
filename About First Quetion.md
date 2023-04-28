# The First Problem

The situation is that a user reached out to notify us that there are several plant records missing farm data. Data about the plants themselves were collected in the field, but information about the farms--like the farm name--was not collected. The user provided a table of the plant records that are missing the farm name. The plant table includes coordinates of the plants. The user wants a table that has the plant data with the farm name included.

We have a farm table that includes the coordinates of the farms. Create a table that displays the plant data and the farm name of the closest farm.

# Input data
There will be 2 text files:
  1. Plant table - This is the plant data collected in the field, including coordinates. 
  2. Farm table - This is the farm data, including farm name and coordinates

# Sample Input
**Plant Table**

     Latitude | Longitude | crop 
     ---|----------|-----------|----------- 
     38.513253 | -90.145310 | corn 
     38.512092 | -90.143185 | soy 
     38.516561 | -90.138432 | wheat

**Farm Table**
 
     Latitude | Longitude | crop 
     ----------|-----------|----------- | ---
     38.520671 | -90.157317 | corn
     38.520671 | -90.157317 | canola
     38.520671 | -90.157317 | wheat
     38.508210 | -90.142351 | corn
     38.508210 | -90.142351 | cotton
     38.515713 | -90.115004 | soybean
     38.515713 | -90.115004 | wheat


# Output Format
     Latitude | Longitude | Farm_Name
     ---|----------|-----------|---
     

