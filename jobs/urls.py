from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('order/', views.OrderList.as_view(), name="orders"),
    path('order/<int:order_id>', views.OrderDetailView.as_view(), name="order_detail"),
    path('addorder', views.AddOrders.as_view(), name="add_order"),
    # path('person/<slug:person_slug>/', views.person, name='person'),
    path('persons/', views.PersonsT.as_view(), name='persons'),
    path('persons/<int:person_id>/', views.PersonDetailView.as_view(), name='person_detail'),
    path('addpersons/', views.AddPersons.as_view(), name='add_person'),
    path('partners/', views.PartnerList.as_view(), name='partners'),
    path('partner/<int:partner_id>/', views.PartnerDetailView.as_view(), name='partner_detail'),
    path('addpartner/', views.AddPartner.as_view(), name='add_partner'),



    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('test/', views.test)

]


