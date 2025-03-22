
from django.urls import path
from .views import BooksListView, BooksDetailView, BookCheckoutView, paymentComplete, SearchResultsListView
from . import views
from django.urls import path
from .views import create_admin

urlpatterns = [
    path('', BooksListView.as_view(), name = 'list'),
    path('<int:pk>/', BooksDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', BookCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
    path('complete/', views.paymentComplete, name='complete'),
    path('payment-success/', views.paymentSuccess, name='payment_success'),  # New success page
    path("create-admin/", create_admin),
]
