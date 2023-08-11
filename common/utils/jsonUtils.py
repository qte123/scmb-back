# JSON工具文件
from django.http import JsonResponse
import json
import numpy as np


# 解决中文乱码
def get_json(json_):
    return JsonResponse(json_, json_dumps_params={'ensure_ascii': False})


# 序列化json
def load_json(request):
    return json.loads(request.body)


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)


def dumps(user):
    user = {"uuid": user.uuid, "username": user.username, "webpath": user.webpath, "user_type": user.user_type.role_id,
            "last_login": user.last_login}
    #data = {"keys": "string", 1: [2, 3], "dict": {"a": "b"}, "key_bytes": b'123'}
    ans = json.dumps(user, cls=Encoder)
    return ans

