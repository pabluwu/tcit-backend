from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class PostView(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        posts_serializer = PostSerializer(posts, many=True)

        return Response(posts_serializer.data)
        
    
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post_data = PostSerializer(post).data 
        post.delete() 
        return Response(post_data, status=status.HTTP_200_OK)  
        

