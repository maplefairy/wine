from .import views
from django.urls import path
app_name = 'book'
urlpatterns = [
    path('', views.allbookscat, name='allbookscat'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_product/', views.add_product, name='add_product'),
    path('<slug:c_slug>/', views.allbookscat, name='books_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.bookdetail, name='bookscatdetail'),

]
