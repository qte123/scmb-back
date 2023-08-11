import json

from django.utils import timezone

from django.db import transaction

from entity.user import User
from common.utils.jsonUtils import get_json, dumps

# 登录
from common.utils.makeUUID import get_uuid


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 创建user对象
    try:
        # 根据username,password从数据库中找到相应的用户记录
        with transaction.atomic():
            user = User.objects.get(username=username, password=password)
            if user.is_activate == 1:
                user.last_login = timezone.now().replace(microsecond=0)
                user.is_online = 1
                token = get_uuid()
                if user.user_type.role_id == 1:
                    menu = [
                        {
                            'path': '/home',
                            'name': 'Home',
                            'label': '',
                            'icon': '',
                            'url': 'home'
                        },
                        {
                            'path': '/search',
                            'name': 'Search',
                            'label': '图片展示',
                            'icon': 'menu',
                            'url': 'search'
                        },
                        {
                            'path': '/upload',
                            'name': 'Upload',
                            'label': '图片上传',
                            'icon': 'folder-add',
                            'url': 'upload'
                        },
                        {
                            'path': '/user',
                            'name': 'User',
                            'label': '用户管理',
                            'icon': 'user',
                            'url': 'user'
                        },
                        {
                            'path': '/images',
                            'name': 'Images',
                            'label': '图片管理',
                            'icon': 'picture',
                            'url': 'images'
                        }
                    ]
                else:
                    menu = [
                        {
                            'path': '/home',
                            'name': 'Home',
                            'label': '',
                            'icon': '',
                            'url': 'home'
                        },
                        {
                            'path': '/search',
                            'name': 'Search',
                            'label': '图片展示',
                            'icon': 'menu',
                            'url': 'search'
                        },
                        {
                            'path': '/upload',
                            'name': 'Upload',
                            'label': '图片上传',
                            'icon': 'folder-add',
                            'url': 'upload'
                        }
                    ]
                user.save()
            else:
                return get_json({'ret': 1, 'msg': '用户已停用'})
    except User.DoesNotExist:
        return get_json({'ret': 1, 'msg': '用户名或密码不正确'})
    user.create_date = str(user.create_date)
    user.modify_date = str(user.modify_date)
    user.last_login = str(user.last_login)
    return get_json({'ret': 0, 'msg': '登录成功', 'menu': menu, 'token': token, 'user': dumps(user)})


# 退出
def logout(request):
    username = request.POST.get('username')
    user = User.objects.get(username=username)
    user.is_online = 0
    user.save()
    return get_json({'ret': 0, 'msg': '退出成功'})
