# This code is sending a message to a DingTalk robot using a webhook. It imports the `requests` and
# `json` modules, defines the webhook URL and headers, and creates a message payload in JSON format.
# Finally, it sends a POST request to the webhook URL with the message payload as the request body.
import requests
import json

# 定义webhook的地址
webhook = "https://oapi.dingtalk.com/robot/send?access_token="
# 定义headers
headers = {"Content-Type": "application/json"}
# 定义text的内容
text = {
    "msgtype": "text",
    "text": {
        "content": "自动提醒：这是一条来自钉钉机器人的消息"
    }
}

# 发送post请求，发送消息
requests.post(url=webhook, headers=headers, data=json.dumps(text))