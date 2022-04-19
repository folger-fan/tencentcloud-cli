**Example 1: 请求浏览数据**



Input: 

```
tccli cat DescribeProbeMetricData --cli-unfold-argument  \
    --AnalyzeTaskType AnalyzeTaskType_Browse \
    --MetricType gauge \
    --Field avg("count") \
    --GroupBy time(1m), "operator" \
    --Filters '"host" = 'default-host'' 'time >= now()-3h'
```

Output: 
```
{
    "Response": {
        "MetricSet": "xx",
        "RequestId": "xx"
    }
}
```
