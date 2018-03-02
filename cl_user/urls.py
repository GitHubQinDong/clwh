from django.conf.urls import url
from cl_user.views import *

urlpatterns = [
    url(r'^login$',login ),
    url(r'^register$',register),
    url(r'^reg_hand$',register_handle),
    url(r'^log_hand',login_handle),
    url(r'^logout',logout),
    url(r'^checkname',register_exist),
    url(r'^userinfo',user_center_info),
    url(r'^userupdate',userupdate),
    url(r'^shdz',shdz),
    url(r'^add_save',add_save),
    url(r'^mrdz',mrdz),
    url(r'^scdz',scdz),
    url(r'^bjdz',bjdz),
]
