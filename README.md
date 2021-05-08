# pay-service
A pay-service for SE2021 at fdu


## API Document 

| API | Method | 
| --- | --- | 
| /api/payment | POST |

#### POST Body:

本接口接受JSON格式的请求体。包括以下三个key:

`invoke_id` : 调用方ID, 仅允许se2021_<组号> 的形式，如 se2021_1, se2021_2, ... se2021_12... se2021_26。

`uid` : 需要进行扣款的用户id.

`amount`: 扣款金额.

需要注意的是，为了模拟现实中场景，本API有一定概率随机返回金额不足的响应，调用方需要对此进行处理。

```json
{
    "invoke_id": "se2021_1",
    "uid": "20212010001",
    "amount": 12.5
}
```



#### Responses:

##### 1. 请求体错误

HTTP Status Code: `400`

Response Body:

```json
{
  "msg": "<具体错误原因>"
}
```

##### 2. 余额不足

HTTP Status Code: `409`

Response Body:

```json
{
  "msg": "failed, the balance is not enough"
}
```

##### 3. 成功

HTTP Status Code: `200`

Response Body:

```json
{
  "msg": "success"
}
```

##### 4. 请求方法错误

使用了除了POST之外的HTTP方法进行请求.

HTTP Status Code: `405`

##### 5. 异常错误

出现了意料之外的错误.

HTTP Status Code: `500`

Response Body:

```json
{
  "msg": "ooooops, there's some exception did't expect. please tell the TA what data you sent.",
}
```

