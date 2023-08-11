# -*- coding: utf-8 -*-
import oss2
from itertools import islice
from img_oss.read_json import read_json

osslist = read_json('img_oss/oss_setting.json')

# 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
auth = oss2.Auth(osslist['accessKeyId'], osslist['accessKeySecret'])
# yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
# 填写Bucket名称。
bucket = oss2.Bucket(auth, osslist['endpoint'], osslist['bucketName'])
# oss用户
oss_user = osslist['oss_user']
# 本地文件存放地址
#filepath = osslist['filepath']
# oss绑定的域名
webpath = osslist['webpath']


# 上传文件
def file_up(filepath,filename):
    # 填写Object完整路径和本地文件的完整路径。Object完整路径中不能包含Bucket名称。
    # 如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
    print(filepath+" "+filename)
    bucket.put_object_from_file(oss_user+"/" + filename, filepath + filename)


# 列举文件
def file_sort():
    # 文件列表
    newlist = []
    # oss2.ObjectIterator用于遍历文件。
    for b in islice(oss2.ObjectIterator(bucket), 1000):
        if b.key[:6] == oss_user + '/' and b.key[6:] != '':
            newlist.append(b.key[6:])
    return newlist


# 获取文件网络地址列表
def file_web_sort():
    newlist = []
    list1 = file_sort()
    for i in range(len(list1)):
        newlist.append(webpath + '/' + oss_user + '/' + list1[i])
    return newlist
