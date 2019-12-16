from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedIdentityField,
                                        SerializerMethodField)
from posts.models import Post,Like
from django.urls import reverse

import json
class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = 'insta-api:post_detail_api',
        lookup_field ='pk',
    )
    user = SerializerMethodField()
    comments = HyperlinkedIdentityField(
        view_name='comments-api:api_list_comments',
        lookup_field='pk',
    )
    likes = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'image',
            'caption',
            'timestamp',
            'updated',
            'comments',
            'likes',
        ]
    def get_user(self, obj):
        account = obj.user.account
        user = {
            "username":obj.user.username,
            "profile":reverse('accounts-api:api_user_detail',kwargs={'pk':obj.user.pk})
        }
        json.dumps(user)
        return user
    def get_likes(self,obj):
        return obj.like_set.count()

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'image',
            'caption',
        ]


class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'user',
            'image',
            'caption',
            'timestamp',
            'updated',
        ]
    def get_user(self, obj):
        return str(obj.user.username)
    def get_image(self, obj):
        try:
            image = obj.image.url 
        except:
            image = None
        return image


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'caption',
            'updated',
        ]
    
class PostLikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ['created']
