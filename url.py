from django.conf.urls import urlfrom django.contrib 
import adminfrom ivr.views
import init_automated_call, handle_user_response
urlpatterns = [   url(r'^admin/', admin.site.urls),   url(r'^gather/$', init_automated_call),   url(r'^respond/$', handle_user_response),]
