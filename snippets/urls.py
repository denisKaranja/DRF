from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

unformated_urlpatterns = [
  # snippets urls
  url(r'^snippets/$', views.SnippetList.as_view()),
  url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
  url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),

  # users urls
  url(r'^users/$', views.UserList.as_view()),
  url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(unformated_urlpatterns)
