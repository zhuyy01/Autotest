import requests

url="http://192.168.179.150/prod-api/system/user"

header={
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjhmNDc5NjQ0LTJiYjEtNGJiZS1hM2M4LTYyZWQ2YzBmZjNkMyJ9.w9MVb1_o45xYK9Yp2k0RoWYautIOIBgLYJEwPPBysD7CzrG2ZtqqvuZHRLHE2UnlBkMbmPHNSWYsCodJcjNvYA"
}

a={"userName": "小六", "nickName": "小六", "password": "123456", "status": "0", "postIds": [], "roleIds": []}

res=requests.post(url=url,json=a,headers=header)
print(res.text)