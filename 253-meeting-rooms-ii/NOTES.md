[[0,30],[5,10],[15,20]]
​
sort the intervals by start time and end time
​
[[0,30],[5,10],[15,20]]
​
heap -
- push (start, end) if heap empty or end > start
- pop if heap not empty and end <= start
keep maxSize of heap -
​
return the maxSize
​
​