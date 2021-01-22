SF Crime Statistics with Spark Streaming

Questions

1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
Changing the values for maxRatePerPartition and maxOffSetPerTrigger can make the value processedRowsPerSecond vary considerably. Higher values for them increases the processedRowsPerSecond until a certain point when the value processedRowsPerSecond starts to decrease.
  

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
I found the most variation when changing these values: maxRatePerPartition and maxOffSetPerTrigger. We can tell the optimal value by checking the values of processedRowsPerSecond and durantionMs values in the progression report.
