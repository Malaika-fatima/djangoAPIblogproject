from django.contrib.auth import get_user_model
from rest_framework import viewsets
#from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer

class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



#code before using viewset the Above code uses viewtset

#class PostList(generics.ListCreateAPIView):
    #queryset = Post.objects.all()
    #serializer_class = PostSerializer

#class PostDetail(generics.RetrieveUpdateDestroyAPIView):
   # permission_classes = (IsAuthorOrReadOnly,) 
    #queryset = Post.objects.all()
    #serializer_class = PostSerializer

#class UserList(generics.ListCreateAPIView): # new
 #   queryset = get_user_model().objects.all()
  #  serializer_class = UserSerializer

#class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
  #  queryset = get_user_model().objects.all()
    #serializer_class = UserSerializer


# Create your views here.
