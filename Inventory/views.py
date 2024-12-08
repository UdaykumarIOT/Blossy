from django.shortcuts import render,redirect
from django.views import View
from .models import Product , Category , CartItem
from django.contrib.auth.mixins import LoginRequiredMixin

class product_list(View):
    def get(self, request):
        products = Product.objects.all()
        context={
            'products': products,
            'items': products
        }
        return render(request, 'products.html', context)
    
    def post(self, request):
        searched_text = request.POST.get('searched_text')
        products = Product.objects.filter(name__icontains=searched_text).all()
        context={
            'products': products,
            'items': Product.objects.all()
        }
        return render(request, 'products.html',context)

class category_list(View):
    def get(self, request):
        categories = Category.objects.all()
        context={
            'categories': categories,
            'items': Product.objects.all()
        }
        return render(request, 'categories.html', context)
    
class category_items(View):
    def get(self, request, id):
        products = Product.objects.filter(category=id).all()
        context={
            'products': products,
            'items': Product.objects.all()
        }
        return render(request, 'products.html', context)

class cart_list(LoginRequiredMixin , View):
    login_url = 'signin'
    
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user).all()
        products = [cart_item.product for cart_item in cart_items]
        grand_total = sum(item.total_price  for item in cart_items )
        
        context={
            'products': products,
            'items': Product.objects.all(),
            'grand_total': grand_total
        }
        return render(request, 'cart.html', context)
    
class cart_add(LoginRequiredMixin, View):
    login_url = 'signin'

    def get(self,request,id):
        product = Product.objects.get(id=id)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        cart_item.update_total_price()
        return redirect('products')