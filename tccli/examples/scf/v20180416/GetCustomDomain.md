**Example 1: 示例1**



Input: 

```
tccli scf GetCustomDomain --cli-unfold-argument  \
    --Domain www.xxx.com
```

Output: 
```
{
    "Response": {
        "CertConfig": {
            "CertificateId": "BfHJsadd7"
        },
        "Domain": "www.xxx.com",
        "EndpointsConfig": [
            {
                "FunctionName": "test1",
                "Namespace": "default",
                "PathMatch": "/cc/",
                "PathRewrite": [
                    {
                        "Path": "/cc/",
                        "Rewrite": "/",
                        "Type": "ExactRules"
                    }
                ],
                "Qualifier": "$LATEST"
            }
        ],
        "Protocol": "HTTP&HTTPS",
        "RequestId": "6941ssdd162b-925f-4c3a-b90f-3558c0aebf97",
        "WafConfig": {
            "WafInstanceId": "",
            "WafOpen": "CLOSE"
        }
    }
}
```
