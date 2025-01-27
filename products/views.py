from django.shortcuts import render, redirect
from django.views.generic import ListView
from products.handler import bot

from products.models import ProductModel,CategoryModel, NewsModel, NewsCategoryModel,CartModel

# def home_page(request):
#     products = ProductModel.objects.all()
#     categories = CategoryModel.objects.all()
#     context = {'products': products,'categories': categories}
#     return render(request, 'index.html', context=context)

class HomePage(ListView):
    template_name = 'index.html'
    model = ProductModel
    context_object_name = 'products'
    paginate_by = 1

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['categories'] = CategoryModel.objects.all()
    return context

def single_news(request, id):
    news = NewsModel.objects.get(id=id)
    context = {'news': news}
    return render(request, 'single-news.html', context=context)




def not_found_page(request):
    return render(request, 'notfound.html')
def news_page(request):
    news = NewsModel.objects.all()
    context = {"news": news}
    return render(request, "about.html", context=context)



def search(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        try:
            exact_product = ProductModel.objects.get(products_name__icontains=get_product)
            return redirect(f'/products/{exact_product.id}')
        except:
            return redirect('notfound')


def product_page(request,id):
    product = ProductModel.objects.get(id=id)
    context = {'product': product}
    return render(request,'single-product.html', context=context)



def about_page(request): # ДОМАШКА
    news_title = NewsModel.objects.all()
    news_categories = NewsCategoryModel.objects.all()
    context = {'news_title': news_title, 'news_categories': news_categories}
    return render(request, 'about.html', context=context)

def izbrannoe(request):
    products = ProductModel.objects.all()
    categories = CategoryModel.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'izbrannoe.html', context=context)

#Функция для добавления товара в корзину
def add_product_to_cart(request,id):
    if request.method == 'POST':
        checker = ProductModel.objects.get(id=id)
        if checker.count >= int(request.POST.get('pr_count')):
            CartModel.objects.create(user_id=request.user.id, user_product=checker,
                                     user_product_quantity=int(request.POST.get('pr_count')))
            print('SUCCESS')
            return redirect('/user_cart')
        else:
            print('ERROR')
            return redirect('/')

def user_cart(request):
    cart = CartModel.objects.filter(user_id=request.user.id)
    if request.method == "POST":
        main_text = 'Новый заказ ока!'

        for i in cart:
            main_text += f'\n Товар: {i.user_product}\n' \
                         f'\n Кол-во: {i.user_product_quantity}\n' \
                         f'\n ID пользователя: {i.user_id}\n' \
                         f'\n Цена: {i.user_product.price}\n'
            bot.send_message(-1002173394684, main_text)
            cart.delete()
            return redirect('/')
    else:
        return render(request, 'cart.html', context={'cart': cart})



