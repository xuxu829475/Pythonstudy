http_status = 400

if http_status == 401:
    print("没有认证")
elif http_status == 400:
    print("请求失败")
elif http_status == 402:
    print("没有授权")
elif http_status == 500:
    print("服务器冒烟了，请稍后再试")
else:
    print("请求成功")
