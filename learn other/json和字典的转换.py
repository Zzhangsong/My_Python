# json字符串转换成字典 json.loads()
import json

ss = '{"mobile_phone": "18600001112", "pwd": "123456789", "type": 1, "reg_name": "美丽可爱的小简","flag":null}'
ss_dict = json.loads(ss)
print(ss_dict)


# 将字典转换成字符串
aa = {'mobile_phone': '18600001112', 'pwd': '123456789', 'type': 1, 'reg_name': '美丽可爱的小简', 'flag': None}
ss_json = json.dumps(aa, ensure_ascii=False)
print(ss_json)