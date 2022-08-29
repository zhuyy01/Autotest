import requests

url="http://192.168.179.150/prod-api/system/user/list"

header={
"Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjhmNDc5NjQ0LTJiYjEtNGJiZS1hM2M4LTYyZWQ2YzBmZjNkMyJ9.w9MVb1_o45xYK9Yp2k0RoWYautIOIBgLYJEwPPBysD7CzrG2ZtqqvuZHRLHE2UnlBkMbmPHNSWYsCodJcjNvYA"
}

reponse=requests.get(url=url,headers=header)
print(reponse.text)