import requests

baseUrl="http://192.168.179.150/prod-api"
url="/system/user/list"    #?pageNum=1&pageSize=10

header={
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjYxOGI0YjFjLTQwMjktNGYwZC04MTdjLTE5MWIzMTBkZTQ3NyJ9.kDOzi1UFhIVFeoDYBCyPfqhy6IfZagvywZqh0za8krNBnN4xo3gwSM9fZ5PO-LjfvqD1PzmHbWZ1rbDBHVv-4g"
    }
response1=requests.get(url=baseUrl+url,headers=header)
print(response1.json())

response1_json = response1.json()

uid=response1_json["rows"][0]["userId"]
url1="/system/user/uid"

head={
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjYxOGI0YjFjLTQwMjktNGYwZC04MTdjLTE5MWIzMTBkZTQ3NyJ9.kDOzi1UFhIVFeoDYBCyPfqhy6IfZagvywZqh0za8krNBnN4xo3gwSM9fZ5PO-LjfvqD1PzmHbWZ1rbDBHVv-4g"
}
response2 = requests.delete(url=baseUrl+url1,headers=head)
print(response2.json())



