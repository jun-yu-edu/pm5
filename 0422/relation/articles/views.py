from django.shortcuts import render
from articles.models import Article, Comment

from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.serializers import ArticleSerializer, CommentSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        # 모든 article 데이터 json으로 응답하기
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, id):
    if request.method == 'GET':
        article = Article.objects.get(id=id)
        serialzer = ArticleSerializer(article)

        return Response(serialzer.data)
    
    elif request.method == 'PUT':
        # 수정을 할꺼야.
        data = request.data
        article = Article.objects.get(id=id)
        serialzer = ArticleSerializer(article, data=data, partial=True)

        if serialzer.is_valid(raise_exception=True):
            serialzer.save()
            return Response(serialzer.data)
        

    elif request.method == 'DELETE':
        article = Article.objects.get(id=id)
        article.delete()
        return Response(status=204)

@api_view(['POST'])
def comment_list(request, article_id):
    data = request.data
    article = Article.objects.get(id=article_id)

    serializer = CommentSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)

        return Response(serializer.data)


@api_view(['PUT'])
def comment_detail(request, article_id, comment_id):
    data = request.data
    comment = Comment.objects.get(id=comment_id)
    serializer = CommentSerializer(comment, data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

