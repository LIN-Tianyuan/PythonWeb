from pay.views import order
from django.conf.urls import url

urlpatterns = [
    # pay/order/
    url(r'^order/$', order)
]