import os
import shutil
from datetime import time

from PIL import Image as imim

from classification import test
from classification.test import init_image_name, change_img_name
from entity.user import User
from common.utils.jsonUtils import get_json

d = 'classification/data/test/'
u = 'user/img_head/'


# 上传用户图片
def upload_image(request):
    username = request.POST.get('username')
    f = request.FILES.get('file')
    i = imim.open(f)
    try:
        i.save(d + str(f))
    except Exception as e:
        print(e)
        shutil.rmtree('classification/data/test/')  # 能删除该文件夹和文件夹下所有文件
        os.mkdir('classification/data/test/')
        return get_json({'ret': 1, 'msg': '图片格式有问题'})
    else:
        test.start_test(username)
        return get_json({'ret': 0, 'msg': '图片上传成功'})


# 上传用户头像
def upload_head(request):
    username = request.POST.get('username')
    print(username)
    f = request.FILES.get('file')
    i = imim.open(f)
    try:
        i.save(u + str(f))
    except Exception as e:
        print(e)
        shutil.rmtree('user/img_head/')  # 能删除该文件夹和文件夹下所有文件
        os.mkdir('user/img_head/')
        return get_json({'ret': 1, 'msg': '图片格式有问题'})
    else:
        init_image_name('user/img_head')
        web = change_img_name('user/img_head', 'user', username)
        user = User.objects.get(username=username)
        user.webpath = web
        user.save()
        shutil.rmtree('user/img_head/')  # 能删除该文件夹和文件夹下所有文件
        os.mkdir('user/img_head/')
        return get_json({'ret': 0, 'msg': '上传成功'})
