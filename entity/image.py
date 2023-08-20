from django.db import models
from entity.user import User


# 图片实体类
class Image(models.Model):
    # uuid
    uuid = models.CharField(max_length=50)
    # 文件名
    filename = models.CharField(max_length=200)
    # 网络地址
    webpath = models.CharField(max_length=250, null=False, blank=False, primary_key=True)
    # 图片类型 0用户照片 1头像
    type = models.PositiveSmallIntegerField(default=0)
    # 图片分类 默认无
    classify = models.CharField(max_length=10, default='')
    # 创建时间
    create_date = models.DateTimeField(null=True)
    # 修改时间
    modify_date = models.DateTimeField(null=True)
    # 上传者
    upload_user = models.ForeignKey(User, on_delete=models.PROTECT)
    # 是否隐藏 0是已隐藏，1是未隐藏
    is_show = models.PositiveSmallIntegerField(default=1)
