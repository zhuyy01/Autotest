import requests

url="http://192.168.179.150/prod-api/system/user/importData?updateSupport=0"

header={
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjhmNDc5NjQ0LTJiYjEtNGJiZS1hM2M4LTYyZWQ2YzBmZjNkMyJ9.w9MVb1_o45xYK9Yp2k0RoWYautIOIBgLYJEwPPBysD7CzrG2ZtqqvuZHRLHE2UnlBkMbmPHNSWYsCodJcjNvYA"
}
f=open(file="C:/Users/朱小小/Desktop/万维传胜OA项目部署步骤(1).doc",mode="rb")
print(f)

j={
    "file":"f"
   }

res=requests.post(url=url,json=j,headers=header)
print(res)