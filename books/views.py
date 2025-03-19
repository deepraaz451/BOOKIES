from django.shortcuts import render 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Book, Order
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
import json



class BooksListView(ListView):
    model = Book
    template_name = 'list.html'


class BooksDetailView(DetailView):
    model = Book
    template_name = 'detail.html'


class SearchResultsListView(ListView):
	model = Book
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Book.objects.filter(
		Q(title__icontains=query) | Q(author__icontains=query)
		)

class BookCheckoutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url     = 'login'


def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Book.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
	)
	return JsonResponse('Payment completed!', safe=False)

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Book, Order

def paymentComplete(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        product_id = data.get('productId')

        product = get_object_or_404(Book, id=product_id)
        Order.objects.create(product=product)

        return JsonResponse({'status': 'success'})  # This tells JavaScript to redirect

def paymentSuccess(request):
    return render(request, 'payment_success.html')  # Renders the success page