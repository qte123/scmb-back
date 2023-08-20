from django.db import models
from django.utils import timezone

from entity.role import Role
from img_oss import oss_control

default_head = oss_control.webpath + '/' + oss_control.oss_user + '/' + 'default.jpg'


# 用户实体类
class User(models.Model):
    # uuid
    uuid = models.CharField(max_length=50)
    # 用户名
    username = models.CharField(max_length=9, primary_key=True)
    # 密码
    password = models.CharField(max_length=20, null=False, blank=False)
    # 用户头像地址
    webpath = models.CharField(max_length=250, null=False, blank=False, default=default_head)
    # 最近登录时间
    last_login = models.DateTimeField(default=timezone.now().replace(microsecond=0))
    # 创建时间
    create_date = models.DateTimeField(null=True)
    # 修改时间
    modify_date = models.DateTimeField(null=True)
    # 用户类型 0普通用户 1管理员
    user_type = models.ForeignKey(Role, on_delete=models.PROTECT)
    # 是否在线
    is_online = models.PositiveSmallIntegerField(default=0)
    # 是否激活  0是停用，1是激活
    is_activate = models.PositiveSmallIntegerField(default=1)
    # 是否隐藏 0是已隐藏，1是未隐藏
    is_show = models.PositiveSmallIntegerField(default=1)
