from django.shortcuts import render
from articles.models import Article
from articles.serializers import ArticleSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def article_list(request):

    articles = Article.objects.all()  # articles : Article 모델에서 가져온 데이터 전체
    serializer = ArticleSerializer(articles, many=True)

    return Response(serializer.data)
