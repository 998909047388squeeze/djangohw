from django.shortcuts import render

from products.models import ProductModel,CategoryModel, NewsModel, NewsCategoryModel
def home_page(request):
    products = ProductModel.objects.all()
    categories = CategoryModel.objects.all()
    context = {'products': products,'categories': categories}
    return render(request, 'index.html', context=context)


def about_page(request): # ДОМАШКА
    news_title = NewsModel.objects.all()
    news_categories = NewsCategoryModel.objects.all()
    context = {'news_title': news_title, 'news_categories': news_categories}
    return render(request, 'about.html', context=context)


