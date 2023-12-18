from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Persons, Partner, Order

# 2.7
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }

    return render(request, 'jobs/index.html', context=data)
def order(request, order_id):
    return HttpResponse(f"Заявки {order_id}")


def person(request, person_slug):
    return HttpResponse("Люди")

def persons_all(request):
    persons = Persons.objects.all()
    return render(request, 'jobs/persons.html', {'persons': persons})



class PersonsT(ListView):
    # model = Women
    template_name = 'jobs/persons.html'
    context_object_name = 'persons'
    title_page = 'Люди'

    # extra_context = {
    #     'title': 'Главная страница',
    #     'menu': menu,
    #     'cat_selected': 0,
    # }

    def get_queryset(self):
        return Persons.objects.all()


class AddPersons(CreateView):
    model = Persons
    fields = '__all__'
    template_name = 'jobs/addperson.html'


class PersonDetailView(DetailView):
    model = Persons
    template_name = 'jobs/person_detail.html'  # имя вашего шаблона
    context_object_name = 'person'
    pk_url_kwarg = 'person_id'  # имя параметра, передающего идентификатор объекта в URL


class PartnerList(ListView):
    # model = Women
    template_name = 'jobs/partners.html'
    context_object_name = 'partners'
    title_page = 'Заказчики'

    # extra_context = {
    #     'title': 'Главная страница',
    #     'menu': menu,
    #     'cat_selected': 0,
    # }

    def get_queryset(self):
        return Partner.objects.all()

class AddPartner(CreateView):
    model = Partner
    fields = '__all__'
    template_name = 'jobs/addpartner.html'


class PartnerDetailView(DetailView):
    model = Partner
    template_name = 'jobs/partner_detail.html'  # имя вашего шаблона
    # context_object_name = 'partner'
    pk_url_kwarg = 'partner_id'


class OrderList(ListView):
    # model = Women
    template_name = 'jobs/orders.html'
    context_object_name = 'orders'
    title_page = 'Заявки'

    # extra_context = {
    #     'title': 'Главная страница',
    #     'menu': menu,
    #     'cat_selected': 0,
    # }

    def get_queryset(self):
        return Order.objects.all()


class AddOrders(CreateView):
    model = Order
    fields = '__all__'
    template_name = 'jobs/addorder.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'jobs/order_detail.html'  # имя вашего шаблона
    context_object_name = 'order'
    pk_url_kwarg = 'order_id'  # имя параметра, передающего идентификатор объекта в URL


def about(request):
    return render(request, 'jobs/about.html', {'title': 'О сайте', 'menu': menu})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Логин")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def test(request):
    return render(request, 'jobs/test.html')