
import requests

url="http://192.168.179.150/prod-api/system/user/importData?updateSupport=0"

header={
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjhkYTQxNWEzLWU2YzQtNDE2My1iZGI1LWFjYWJjYjE3NjJiOCJ9.gDg4_9yHM6tKriF9a1HJVkEF2XGVcbNJAjS7MELzU8sk3KexcABxiS1pcp-_ZuCfBgZTmG6Gmbx5wGuH7eqdZQ",
    "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundary2HblYe21VrvA5cdt",
    "Cookie":"username=admin; rememberMe=true; password=M5dWXJ31H9WAp8kFAyqTw7lSb7oGodB2DOUrrEeIAH4zNMU2b3rSDQJPNXaQza3njoZRJGgRhk45ZgCZMEL8EA==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjhkYTQxNWEzLWU2YzQtNDE2My1iZGI1LWFjYWJjYjE3NjJiOCJ9.gDg4_9yHM6tKriF9a1HJVkEF2XGVcbNJAjS7MELzU8sk3KexcABxiS1pcp-_ZuCfBgZTmG6Gmbx5wGuH7eqdZQ; sidebarStatus=0"
}
f=open(file="C:/Users/朱小小/Desktop/移动端通用测试点.xls",mode="rb")
print(f)

fil={
    "file":f
}

res=requests.post(url=url,data=fil,headers=header,timeout=0.0000001)

print(res.json())