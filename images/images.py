from django.db import transaction
from django.utils import timezone
from entity.image import Image
from entity.user import User
from common.utils.handler import dispatcherBase
from common.utils.jsonUtils import get_json
from common.utils.makeUUID import get_uuid
from common.utils.querySetSlice import query_slice
from common.config import trains_type_list


def dispatcher(request):
    return dispatcherBase(request, Action2Handler)


# 获取图片分类类型列表
def get_classify_list(request):
    retlist = trains_type_list
    return get_json({'ret': 0, 'retlist': retlist})


# 获取图片信息列表
def get_image_list(request):
    username = request.POST.get('username')
    classify = request.POST.get('classify')
    if username == '' and classify == '':
        qs = query_slice(Image.objects.filter(type=0, is_show=1).order_by('-create_date').values(), '')
    elif username == '' and classify != '':
        qs = query_slice(
            Image.objects.filter(type=0, classify=classify, is_show=1).order_by('-create_date').values(), '')
    elif username != '' and classify == '':
        qs = query_slice(
            Image.objects.filter(upload_user_id=username, type=0, is_show=1).order_by('-create_date').values(), '')
    else:
        qs = query_slice(
            Image.objects.filter(upload_user_id=username, classify=classify, type=0, is_show=1).order_by(
                '-create_date').values(), '')
    retlist = list(qs)
    for i in range(len(retlist)):
        retlist[i]['upload_user'] = str(retlist[i]['upload_user_id'])
        retlist[i]['create_date'] = str(retlist[i]['create_date'])
        retlist[i]['modify_date'] = str(retlist[i]['modify_date'])
    return get_json({'ret': 0, 'retlist': retlist})


# 获取所有图片
def get_images_list(request):
    classify = request.POST.get('classify')
    page = request.POST.get('page')
    if classify == '':
        qs = query_slice(Image.objects.filter(is_show=1).order_by('-create_date').values(), '')
    else:
        qs = query_slice(Image.objects.filter(classify=classify, is_show=1).order_by('-create_date').values(), '')
    retlist = list(qs)
    newlist = []
    for i in range(len(retlist)):
        filename = retlist[i]['filename']
        webpath = retlist[i]['webpath']
        if retlist[i]['type'] == 0:
            type = '用户图片'
        else:
            type = '用户头像'
        classify = retlist[i]['classify']
        add_date = str(retlist[i]['create_date'])
        upload_user = retlist[i]['upload_user_id']
        newlist.append(
            {'filename': filename, 'webpath': webpath, 'type': type, 'classify': classify, 'add_date': add_date,
             'upload_user': upload_user})
    return get_json({'ret': 0, 'retlist': newlist, 'total': get_total()})


# 获取当前用户头像
def get_head(request):
    username = request.POST.get('username')
    user = User.objects.get(username=username)
    webpath = user.webpath
    return get_json({'ret': 0, 'webpath': webpath})


# 删除（隐藏）图片
def delete_image(request):
    username = request.POST.get('username')
    filename = request.POST.get('filename')
    address = request.POST.get('address')
    type = request.POST.get('type')
    print(type)
    print(username)
    flag = False
    try:
        # 根据Cno从数据库中找到相应的课程记录
        with transaction.atomic():
            image = Image.objects.get(filename=filename, upload_user_id=username)
            if address == 'image' and type == '用户头像':
                try:
                    user = User.objects.get(webpath=image.webpath)
                except User.DoesNotExist:
                    flag = True
                    image.is_show = 0
                    image.modify_date = timezone.now().replace(microsecond=0)
                else:
                    return get_json({'ret': 1, 'msg': '头像正在被用户使用，不能删除'})
            else:
                flag = True
                image.is_show = 0
                image.modify_date = timezone.now().replace(microsecond=0)
    except Image.DoesNotExist:
        return get_json({'ret': 1, 'msg': '删除失败'})
    if flag:
        image.save()
        return get_json({'ret': 0, 'msg': '删除成功'})
    else:
        return get_json({'ret': 1, 'msg': '删除失败'})


# 修改图片信息
def modify_image(request):
    filename = request.POST.get('filename')
    classify = request.POST.get('classify')
    print(filename)
    flag = False
    try:
        # 根据Cno从数据库中找到相应的课程记录
        with transaction.atomic():
            flag = True
            image = Image.objects.get(filename=filename)
            image.classify = classify
            image.modify_date = timezone.now().replace(microsecond=0)
    except Image.DoesNotExist:
        return get_json({'ret': 1, 'msg': '修改失败'})
    if flag:
        image.save()
        return get_json({'ret': 0, 'msg': '修改成功'})
    else:
        return get_json({'ret': 1, 'msg': '修改失败'})


def get_images_num(request):
    retlist = []
    username = request.POST.get('username')
    for i in range(1, len(trains_type_list)):
        retlist.append(
            {'type': trains_type_list[i]['label'], 'total': get_image_message(username, trains_type_list[i]['value'])})
    return get_json({'ret': 0, 'retlist': retlist})


# 获取所有照片总数
def get_total():
    return Image.objects.all().count()


# 获取照片数据统计信息
def get_image_message(username, classify):
    if classify == '':
        return Image.objects.filter(upload_user_id=username, type=0, is_show=1).count()
    else:
        return Image.objects.filter(upload_user_id=username, classify=classify, type=0, is_show=1).count()


# 添加图片
def add_img(filename, webpath, type, classify, upload_user):
    image = Image.objects.create(uuid=get_uuid(), filename=filename, webpath=webpath,
                                 type=type, classify=classify, create_date=timezone.now().replace(microsecond=0),
                                 upload_user_id=upload_user)


Action2Handler = {
    'get_classify_list': get_classify_list,
    'get_image_list': get_image_list,
    'get_images_list': get_images_list,
    'get_head': get_head,
    'delete_image': delete_image,
    'modify_image': modify_image,
    'get_images_num': get_images_num,
}
