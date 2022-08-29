import requests
import time

baseUrl="https://api.didiyun.com"
list="/dicloud/i/compute/dc2/list"

start="/dicloud/i/compute/dc2/start"
stop="/dicloud/i/compute/dc2/stop"

if __name__ == '__main__':
    header={
    "Accept":"Accept: application/json, text/plain, */*",
    "Content-Type":"Content-Type: application/json;charset=UTF-8",
    "Cookie":"Hm_lvt_9eaa41ddde51c419f3c8953af0161d25=1660038268,1660719111,1660748148,1661453249; u_name=186*****374; Hm_lpvt_9eaa41ddde51c419f3c8953af0161d25=1661453288; feq=1; q=7rkE0H7OZHJ2O2sbamgu5AgJancQYlLMEhJ6BYNGIqEkzLuNAkEMgOFe_tha2eN5Or38eriD5ZEMEohotb0joIFvYyqBL7oowjTChJkIH2pFmE6oMDNhtSbT0a0JsxD8_CL8ESD8E71l96S1jJ5GUhWOhOcmrMTG4_a8H1ai7MLpo1nRom_tTGC9qvfWvWWEy1e9Erq_AgAA__8=",
    "Dicloud-Header-Csrf-Token":"6QdNpyA-t_eQsBBz8v9ZuHqnTH8:1661505017572"
}
    j1={"start": 0, "limit": 10, "simplify": False, "condition": {}}

    res1=requests.post(url=baseUrl+list,json=j1,headers=header)
    print("第一个请求的请求参数为:",res1.text)

    res1_json=res1.json()
    # data_list = res1_json["data"]
    # dc2=data_list[0]
    # print(dc2)
    # UUid=dc2["dc2Uuid"]
    # print(UUid)

    UUid=res1_json["data"][0]["dc2Uuid"]
    print(UUid)

    #data[0].dc2Uuid

    j2={"dc2": [{"dc2Uuid": UUid}]}

    res2=requests.post(url=baseUrl+stop,json=j2,headers=header)
    print("这是第二个接口的响应数据:",res2.json())

    print("*******")
    time.sleep(15)
    print("睡眠结束,一共睡眠15秒")

    j3={"dc2": [{"dc2Uuid": UUid}]}
    res3=requests.post(url=baseUrl+start,json=j3,headers=header)
    print("这是第三个接口响应数据,:",res3.json())