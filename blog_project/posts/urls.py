from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.url




#this code is beforing using routers the above code uses router
#from .views import UserList, UserDetail, PostList, PostDetail

#urlpatterns = [
 #  path('users/<int:pk>/', UserDetail.as_view()),
  #  path('<int:pk>/', PostDetail.as_view()),
   # path('', PostList.as_view()),
#]