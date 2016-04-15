from django.conf.urls import url
from scholarship import views

urlpatterns = [
	url(r'^scholarships/$', views.scholarship_list),
	url(r'^scholarships/(?P<pk>[0-9]+)/$', views.scholarship_details)
]