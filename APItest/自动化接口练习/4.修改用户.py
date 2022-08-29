import requests

url="http://192.168.179.150/prod-api/system/user"

header={
    "Content-Type":"application/json;charset=UTF-8",
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjVkMTFlMTg5LTM0YzUtNGY5Ni05ZTQwLWFkZjI4YTczMmUyMiJ9.Q0jaGI_RKuc515KQYMZrDd32QW50z_QyEzMx7WwVpzKUcVRNfPWPD1yzH77nhpeI3cxdgMkLZA0wXv_2PyG4hA"
}

data={"searchValue":None,"createBy":"admin","createTime":"2022-08-25 13:19:50","updateBy":None,"updateTime":None,"remark":None,"params":{},"userId":7,"deptId":100,"userName":"小朱","nickName":"333","email":"","phonenumber":"15138296808","sex":"0","avatar":"","salt":None,"status":"0","delFlag":"0","loginIp":"","loginDate":None,"dept":{"searchValue":None,"createBy":None,"createTime":None,"updateBy":None,"updateTime":None,"remark":None,"params":{},"deptId":100,"parentId":0,"ancestors":"0","deptName":"万维传胜","orderNum":"0","leader":"小维","phone":None,"email":None,"status":"0","delFlag":None,"parentName":None,"children":[]},"roles":[],"roleIds":[],"postIds":[2],"roleId":None,"admin":False,"password":""}

res=requests.put(url=url,json=data,headers=header)
print(res.json())

