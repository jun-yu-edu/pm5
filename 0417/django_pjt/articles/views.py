from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from articles.models import Article, Person

def articles(request):
    return HttpResponse('서버에서 보낸 정보')

def create(request):
    article = Article(title='제목', content='내용')
    article.save()

    return HttpResponse(article )

def read(request):
    articles = Article.objects.all()

    return HttpResponse(articles)


def read_id(request, id):

    article = Article.objects.get(id=id)

    return HttpResponse(article)


def create_person(request):
    person = Person(name='이름')
    person.save()
    return HttpResponse(person)

def read_person(request):
    person = Person.objects.all()

    return HttpResponse(person)

def read_id_person(request, id):

    person = Person.objects.get(id=id)

    return HttpResponse(person)
