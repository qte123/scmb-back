from django.db import transaction

from entity.image import Image
from entity.user import User
from common.utils.handler import dispatcherBase
from django.utils import timezone

from common.utils.jsonUtils import get_json
from common.utils.querySetSlice import query_slice
from images.images import get_image_message
from common.config import initial_password, vip_code


def dispatcher(request):
    return dispatcherBase(request, Action2Handler)


# 获取用户列表
def get_user_list(request):
    username = request.POST.get('username')
    user_type = request.POST.get('user_type')
    if user_type == '' and username == '':
        qs = query_slice(User.objects.filter(is_show=1).values(), '')
    elif user_type != '' and username == '':
        qs = query_slice(User.objects.filter(user_type_id=user_type, is_show=1).values(), '')
    elif user_type == '' and username != '':
        qs = query_slice(User.objects.filter(username__contains=username, is_show=1).values(), '')
    else:
        qs = query_slice(User.objects.filter(username__contains=username, user_type_id=user_type, is_show=1).values(),
                         '')
    retlist = list(qs)
    newlist = []
    for i in range(len(retlist)):
        username = retlist[i]['username']
        password = retlist[i]['password']
        imgTotal = get_image_message(username, '')
        if retlist[i]['user_type_id'] == 0:
            type = '普通用户'
        else:
            type = '管理员'
        last_login = str(retlist[i]['last_login'])
        add_date = str(retlist[i]['create_date'])
        modify_date = str(retlist[i]['modify_date'])
        if retlist[i]['is_activate'] == 1:
            status = '启用'
        else:
            status = '停用'
        if retlist[i]['is_online'] == 1:
            line = '在线'
        else:
            line = '离线'
        newlist.append(
            {'username': username, 'password': password, 'imgTotal': imgTotal, 'type': type, 'last_login': last_login,
             'add_date': add_date, 'modify_date': modify_date, 'status': status, 'line': line})
    return get_json({'ret': 0, 'retlist': newlist})


# 删除（停用）用户
def delete_user(request):
    username = request.POST.get('username')
    flag = False
    try:
        # 根据Cno从数据库中找到相应的课程记录
        with transaction.atomic():
            user = User.objects.get(username=username)
            if user.is_online != 1:
                flag = True
                user.is_show = 0
                user.is_activate = 0
                user.is_online = 0
                user.modify_date = timezone.now().replace(microsecond=0)
            else:
                return get_json({'ret': 1, 'msg': '修改的用户当前在线，禁止修改信息'})
    except User.DoesNotExist:
        return get_json({'ret': 1, 'msg': '删除失败'})
    if flag:
        qs = query_slice(Image.objects.filter(is_show=1, upload_user_id=user.username).values(), '')
        retlist = list(qs)
        print(retlist)
        for i in range(len(retlist)):
            filename = retlist[i]['filename']
            image = Image.objects.get(filename=filename)
            image.is_show = 0
            image.save()
        user.save()
        return get_json({'ret': 0, 'msg': '删除成功'})
    else:
        return get_json({'ret': 1, 'msg': '删除失败'})


# 修改用户信息
def modify_user(request):
    username = request.POST.get('username')
    user_type = request.POST.get('type')
    status = request.POST.get('status')
    flag = False
    if user_type == '普通用户':
        user_type = 0
    else:
        user_type = 1
    if status == '启用':
        status = 1
    else:
        status = 0
    try:
        # 根据Cno从数据库中找到相应的课程记录
        with transaction.atomic():
            user = User.objects.get(username=username)
            if user.is_online != 1:
                flag = True
                user.user_type.role_id = user_type
                user.is_activate = status
                user.modify_date = timezone.now().replace(microsecond=0)
            else:
                return get_json({'ret': 1, 'msg': '修改的用户当前在线，禁止修改信息'})
    except User.DoesNotExist:
        return get_json({'ret': 1, 'msg': '修改失败'})
    if flag:
        user.save()
        return get_json({'ret': 0, 'msg': '修改成功'})
    else:
        return get_json({'ret': 1, 'msg': '修改失败'})


# 修改用户密码
def modify_password(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    flag = False
    try:
        # 根据Cno从数据库中找到相应的课程记录
        with transaction.atomic():
            user = User.objects.get(username=username)
            flag = True
            user.password = password
            user.modify_date = timezone.now().replace(microsecond=0)
    except User.DoesNotExist:
        return get_json({'ret': 1, 'msg': '用户名不存在'})
    if flag:
        user.save()
        return get_json({'ret': 0, 'msg': '修改成功'})
    else:
        return get_json({'ret': 1, 'msg': '修改失败'})


# 重置用户密码
def reset_password(request):
    username = request.POST.get('username')
    address = request.POST.get('address')
    code = request.POST.get('code')
    flag = False
    try:
        # 根据Cno从数据库中找到相应的课程记录
        with transaction.atomic():
            user = User.objects.get(username=username)
            if user.is_online != 1:
                if address == 'login':
                    if code == vip_code:
                        flag = True
                        user.password = initial_password
                        user.modify_date = timezone.now().replace(microsecond=0)
                    else:
                        return get_json({'ret': 1, 'msg': '邀请码错误'})
                else:
                    flag = True
                    user.password = initial_password
                    user.modify_date = timezone.now().replace(microsecond=0)
            else:
                return get_json({'ret': 1, 'msg': '该用户当前在线，禁止重置密码'})
    except User.DoesNotExist:
        return get_json({'ret': 1, 'msg': '用户名不存在'})
    if flag:
        user.save()
        return get_json({'ret': 0, 'msg': '重置成功'})
    else:
        return get_json({'ret': 1, 'msg': '重置失败'})


# 获取用户类别
def get_user_type(request):
    retlist = [{'label': '全部', 'value': ''}, {'label': '普通用户', 'value': 0}, {'label': '管理员', 'value': 1}]
    return get_json({'ret': 0, 'retlist': retlist})


Action2Handler = {
    'get_user_list': get_user_list,
    'delete_user': delete_user,
    'modify_user': modify_user,
    'modify_password': modify_password,
    'reset_password': reset_password,
    'get_user_type': get_user_type,
}
