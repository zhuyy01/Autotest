import requests

url="http://192.168.179.150/prod-api/system/role/list"

head={
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjYxOGI0YjFjLTQwMjktNGYwZC04MTdjLTE5MWIzMTBkZTQ3NyJ9.kDOzi1UFhIVFeoDYBCyPfqhy6IfZagvywZqh0za8krNBnN4xo3gwSM9fZ5PO-LjfvqD1PzmHbWZ1rbDBHVv-4g"
}

res=requests.get(url=url,headers=head)
print((res.text))
