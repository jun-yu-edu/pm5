from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {"article": {"read_only": True}}


class ArticleSerializer(serializers.ModelSerializer):


    class CommentSerializer(serializers.ModelSerializer):

        class Meta:
            model = Comment
            # fields = '__all__'
            fields = ['id', 'content']
        

    comment_set = CommentSerializer(many=True, required=False)

    class Meta:
        model = Article
        fields = '__all__'
