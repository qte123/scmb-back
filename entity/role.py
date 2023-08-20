from django.db import models


# 角色实体类
class Role(models.Model):
    # 角色编号
    role_id = models.PositiveSmallIntegerField(primary_key=True)
    # 角色名称
    role_name = models.CharField(max_length=6, null=False, blank=False)
