import requests
baseUrl="https://api.didiyun.com/"

url="dicloud/i/compute/dc2/list"

head={
    "Accept":"Accept: application/json, text/plain, */*",
    "Content-Type":"Content-Type: application/json;charset=UTF-8",
    "Cookie":"Hm_lvt_9eaa41ddde51c419f3c8953af0161d25=1660038268,1660719111,1660748148,1661453249; u_name=186*****374; Hm_lpvt_9eaa41ddde51c419f3c8953af0161d25=1661453288; feq=1; q=S45oBuJRPLUunUjUXVcD6hH6v0qlJyhxuSHoK2JCoqUkzLuNAkEMgOFe_tha2eN5Or38eriD5ZEMEohotb0joIFvYyqBL7oowjTChJkIH2pFmE6oMDNhtSbT1iwLsxD8_CL8ESD8E71l96S1jJ5GUhWOhGcXVmLjcXveDytRduH00axoGm_tTGC9qvfWvWWEy1e9Erq_AgAA__8=",
    #"Cookie":"Hm_lvt_9eaa41ddde51c419f3c8953af0161d25=1660038268,1660719111,1660748148,1661453249; u_name=186*****374; Hm_lpvt_9eaa41ddde51c419f3c8953af0161d25=1661453288; q=QJ9CAltpBX-cF0MyiqL6g1zAPsR3D0y3gzGLxTmmfKEkzDuOwjAQgOG7_PUomoftONNuv3fYhfBojASiinJ3BFzg2xhKEpNOijCMNGE4GYtaFUaQKoxCWmuutZsXYVSSn1-EPxKEf7LPJcK11aX74qrCkYxwYSU3Hrfn_bCSdRdOH81KjXhrZxLrTaPPPeaCcPmqV1L3VwAAAP__; feq=1",
    # "Dicloud-Header-Csrf-Token":"gW6OU_xLIUJT6Mi_P1HmkRL7-5g:1661453324795"
    "Dicloud-Header-Csrf-Token":"inQqQ1cFSF5sg-zNNeU1KDih5YU:1661502914808"
}

data_request={"start": 0, "limit": 10, "simplify": False, "condition": {}}

res=requests.post(url=baseUrl+url,json=data_request,headers=head)
print(res.status_code)  # 响应状态码
p=res.raw.read()
print(res.content)
print(p)


print("text文本形式查看响应数据",res.text)
print("json形式查看响应数据",res.json())