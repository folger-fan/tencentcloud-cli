**Example 1: 删除边缘容器CVM实例**

删除边缘容器CVM实例

Input: 

```
tccli tke DeleteEdgeCVMInstances --cli-unfold-argument  \
    --ClusterID cls-xxxxx \
    --CvmIdSet ecm-xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "187c16d5-1f53-4e88-b684-077f0c7369b2"
    }
}
```
