# app/urls.py




from django.conf.urls import url

from app import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test/$', views.test, name='test'),
  url(r'^profile/$', views.profile, name='profile'),
  url(r'^devices/$', views.devices, name='devices'),
  url(r'^sigfox/$', views.sigfox, name='sigfox'),
  url(r'^webhook', views.webhook, name='webhook'),
  url(r'^sigfox_webhook', views.sigfox_webhook, name='sigfox_webhook'),
  url(r'^sigfox_iot', views.sigfox_iot, name='sigfox_iot'),

]

