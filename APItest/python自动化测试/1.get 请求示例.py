import requests

url="http://v.juhe.cn/toutiao/index"

P = {
"key":"d9b19f0e2fe105fd79a66a6228b78ec0",
"type":"tiyu"
}


reponse=requests.get(url=url,params=P)
print(reponse.text)