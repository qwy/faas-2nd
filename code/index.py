# 导入必要的库
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import datetime

# 创建FastAPI应用实例
app = FastAPI()

# 定义根路由
@app.get("/")
async def hello():
    # 返回HTML响应
        return HTMLResponse(
        """<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>Serverless Devs - Powered By Serverless Devs</title>
    <link href="https://example-static.oss-cn-beijing.aliyuncs.com/web-framework/style.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<div class="website">
    <div class="ri-t">
        <h1>Devsapp</h1>
        <h2>这是一个 FastAPI 项目</h2>
        <span>自豪地通过Serverless Devs进行部署</span>
        <br/>
        <p>您也可以快速体验： <br/>
            • 下载Serverless Devs工具：npm install @serverless-devs/s<br/>
            • 初始化项目：s init start-fastapi-v3<br/>

            • 项目部署：s deploy<br/>
            <br/>
            Serverless Devs 钉钉交流群：33947367
        </p>
    </div>
</div>
</body>
</html>
"""
    )


# 新增hi路由
@app.get("/hi")
async def hi():
    return HTMLResponse(
        """
        <html>
        <head>
            <title>Hi页面</title>
            <script>
            function showInfo() {
                // 获取本地时间
                var localTime = new Date().toLocaleString();
                // 发送请求获取服务器时间
                fetch('/server_time')
                    .then(response => response.text())
                    .then(serverTime => {
                        // 显示时间信息
                        document.getElementById('info').innerHTML = 
                            '本地时间: ' + localTime + '<br>' +
                            '服务器时间: ' + serverTime;
                    });
            }
            </script>
        </head>
        <body>
            <h1>欢迎来到Hi页面</h1>
            <button onclick="showInfo()">显示时间信息</button>
            <div id="info"></div>
        </body>
        </html>
        """
    )

# 新增获取服务器时间的路由
@app.get("/server_time")
async def server_time():
    # 返回服务器当前时间
    return str(datetime.datetime.now())

# 主程序入口
if __name__ == "__main__":
    # 运行uvicorn服务器
    uvicorn.run(app, host="0.0.0.0", port=9000)
