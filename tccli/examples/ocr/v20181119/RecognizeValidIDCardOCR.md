**Example 1: 有效身份证件识别（鉴伪版）示例**

识别身份证信息

Input: 

```
tccli ocr RecognizeValidIDCardOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/IDCardOCR/IDCardOCR1.jpg
```

Output: 
```
{
    "Response": {
        "IDCardInfo": {
            "Address": {
                "Confidence": 89,
                "Content": "广东省深圳市南山区腾讯大厦",
                "IsInComplete": 0,
                "IsReflect": 0
            },
            "Authority": {
                "Confidence": 0,
                "Content": "",
                "IsInComplete": 1,
                "IsReflect": 0
            },
            "Birth": {
                "Confidence": 89,
                "Content": "1995年5月13日",
                "IsInComplete": 0,
                "IsReflect": 0
            },
            "CardImage": {
                "Confidence": 0,
                "Content": "",
                "IsInComplete": 1,
                "IsReflect": 0
            },
            "IdNum": {
                "Confidence": 89,
                "Content": "440305199505132561",
                "IsInComplete": 0,
                "IsReflect": 0
            },
            "Name": {
                "Confidence": 89,
                "Content": "刘洋",
                "IsInComplete": 0,
                "IsReflect": 0
            },
            "Nation": {
                "Confidence": 89,
                "Content": "汉",
                "IsInComplete": 0,
                "IsReflect": 0
            },
            "PortraitImage": {
                "Confidence": 0,
                "Content": "",
                "IsInComplete": 1,
                "IsReflect": 0
            },
            "Sex": {
                "Confidence": 89,
                "Content": "女",
                "IsInComplete": 0,
                "IsReflect": 0
            },
            "ValidDate": {
                "Confidence": 0,
                "Content": "",
                "IsInComplete": 1,
                "IsReflect": 0
            },
            "WarnInfos": {
                "BorderCheck": 0,
                "CopyCheck": 0,
                "OcclusionCheck": 0,
                "PSCheck": 0,
                "ReshootCheck": 0
            }
        },
        "PermanentResidencePermitInfo": null,
        "RequestId": "531e2077-4fc0-4245-9114-526a752f71a8",
        "ResidencePermitInfo": null,
        "TemporaryIDCardInfo": null,
        "Type": "身份证人像面"
    }
}
```
