from django.apps import AppConfig


class SimpleauthConfig(AppConfig):
    name = 'apps'

    def ready(self):
        """
        在子类中重写此方法，以便在Django启动时运行代码。
        :return:
        """
        from entity.role import Role
        try:
            user = Role.objects.get(role_id=0)
        except Role.DoesNotExist:
            Role.objects.create(role_id=0, role_name='user')
        try:
            admin = Role.objects.get(role_id=1)
        except Role.DoesNotExist:
            Role.objects.create(role_id=1, role_name='admin')
