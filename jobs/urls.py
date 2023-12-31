from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('order/<int:order_id>', views.order, name="order"),
    path('person/<slug:person_slug>/', views.person, name='person'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),

]