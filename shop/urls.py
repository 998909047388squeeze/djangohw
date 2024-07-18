from django.contrib import admin
from django.urls import path


from django.conf.urls.static import static
from django.conf import settings

from products.views import HomePage, about_page, not_found_page, search,product_page, add_product_to_cart, user_cart, news_page, izbrannoe, single_news
from users.views import register_view, login_view, profile_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('about/', news_page), #ДОМАШКА
    path('signup', register_view, name='signup'),
    path('login', login_view, name='login'),
    path('profile', profile_view, name='profile'),
    path('logout', logout_view, name='logout'),
    path('search', search),
    path('products/<int:id>',product_page),
    path('notfound', not_found_page, name='notfound'),
    path('add_to_cart/<int:id>', add_product_to_cart),
    path('user_cart', user_cart, name='user_cart'),
    path('izbrannoe', izbrannoe,  name='izbrannoe'),
    path('single_news/<int:id>', single_news, name='single_news'),

]
#/media/product.png,
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#/static/hello.js
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
