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
<!-- ... 原有的HTML内容 ... -->
</html>
"""
    )

# 新增hi路由
@app.get("/hi")
async def hi():
    # 返回带有按钮的HTML页面
    return HTMLResponse(
        """
        <html>
        <head>
            <title>Hi页面</title>
            <script>
            function showInfo() {
                // 获取本地时间
                var localTime = new Date().toLocaleString();
                // 获取位置信息（需要用户授权）
                navigator.geolocation.getCurrentPosition(function(position) {
                    var lat = position.coords.latitude;
                    var lon = position.coords.longitude;
                    // 发送请求获取服务器时间
                    fetch('/server_time')
                        .then(response => response.text())
                        .then(serverTime => {
                            // 显示所有信息
                            document.getElementById('info').innerHTML = 
                                '本地时间: ' + localTime + '<br>' +
                                '位置: 纬度 ' + lat + ', 经度 ' + lon + '<br>' +
                                '服务器时间: ' + serverTime;
                        });
                });
            }
            </script>
        </head>
        <body>
            <h1>欢迎来到Hi页面</h1>
            <button onclick="showInfo()">显示信息</button>
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
