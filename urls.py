from django.conf.urls import url,include
from rest_framework import routers
from . import views
from django.urls import path,include
from rest_framework.schemas import get_schema_view

router=routers.DefaultRouter()
router.register('books',views.descriptionview)
schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
      path ('',include(router.urls))
      
     ]
