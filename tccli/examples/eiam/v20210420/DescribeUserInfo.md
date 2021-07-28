**Example 1: 请求示例**



Input: 

```
tccli eiam DescribeUserInfo --cli-unfold-argument  \
    --UserName xxx
```

Output: 
```
{
    "Response": {
        "UserName": "xx",
        "Status": "xx",
        "DisplayName": "xx",
        "Description": "xx",
        "UserGroupIds": [
            "xx",
            "xx"
        ],
        "UserId": "xx",
        "ActivationTime": "xx",
        "Phone": "xx",
        "OrgNodeId": "xx",
        "DataSource": "xx",
        "ExpirationTime": "xx",
        "Email": "xx",
        "RequestId": "xx"
    }
}
```
