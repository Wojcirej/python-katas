# Total amount of points

### Description
Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the array.
Write a function that takes such list and counts the points of our team in the championship. Rules for counting points for each match:
* if x>y - 3 points
* if x<y - 0 point
* if x=y - 1 point
#### Notes
* there are 10 matches in the championship
* 0 <= x <= 4
* 0 <= y <= 4

### Examples
```python
total_amount_of_points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']) #=> 30
total_amount_of_points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']) #=> 10
total_amount_of_points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']) #=> 0
total_amount_of_points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']) #=> 15
total_amount_of_points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']) #=> 12
```

### Link to kata on codewars.com
https://www.codewars.com/kata/5bb904724c47249b10000131
