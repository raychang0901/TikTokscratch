import json
uid_li = []
def anls(str_data):
    js_data = json.loads(str_data,strict = 'false')
    following_li = js_data['followings']
    with open('uid.txt', 'a+', encoding='utf-8') as f:
        for ele in following_li:
           f.write(ele['uid'] + '\n')
