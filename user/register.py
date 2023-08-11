# 注册用户
from django.utils import timezone

from django.db import transaction

from entity.user import User
from entity.role import Role
from common.utils.jsonUtils import get_json
from common.utils.makeUUID import get_uuid
from common.config import vip_code
from img_oss import oss_control

default_head = oss_control.webpath + '/' + oss_control.oss_user + '/' + 'default.jpg'

def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_type = request.POST.get('userType')
    code = request.POST.get('code')
    print(user_type)
    print(code)
    flag = False
    if (username is not None and username != '') and (password is not None and password != ''):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            flag = True
        if flag:
            try:
                with transaction.atomic():
                    role = Role.objects.get(role_id=int(user_type))
                    if role.role_id == 1:
                        if code == vip_code:
                            user1 = User.objects.create(uuid=get_uuid(), username=username, password=password,
                                                        user_type=role,
                                                        create_date=timezone.now().replace(microsecond=0))
                        else:
                            return get_json({'ret': 1, 'msg': '邀请码不正确'})
                    else:
                        user1 = User.objects.create(uuid=get_uuid(), username=username, password=password,
                                                    user_type=role,
                                                    create_date=timezone.now().replace(microsecond=0))
                return get_json({'ret': 0, 'msg': '注册成功'})
            except Exception as e:
                print(e)
                return get_json({'ret': 1, 'msg': '注册失败'})

        else:
            return get_json({'ret': 1, 'msg': '用户已存在'})
    else:
        return get_json({'ret': 1, 'msg': '用户名或密码为空'})
