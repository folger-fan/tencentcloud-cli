**Example 1: 查看添加子域名 Zone 域解析 TXT 记录值验证状态参数示例**

查看添加子域名 Zone 域解析 TXT 记录值验证状态

Input: 

```
tccli dnspod DescribeSubdomainValidateStatus --cli-unfold-argument  \
    --DomainZone sub.dnspod.cn
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```
