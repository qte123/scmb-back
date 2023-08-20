from django.urls import path
from user import user
from user import register
from user import login_out

urlpatterns = [
    # 副路由表
    path('do/', user.dispatcher),
    path('register/', register.register),
    path('login/', login_out.login),
    path('logout/', login_out.logout),

]
