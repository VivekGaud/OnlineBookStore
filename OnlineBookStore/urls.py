"""OnlineBookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from books import views 
from users import views as users_view
from cart import views as cart_view
from OnlineBookStore import views as index_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index_view.index, name="homepage"),
    url(r'^books/', include('books.urls')),

    url(r'^register/',users_view.register, name = "register" ),
    url(r'^login/',users_view.user_login, name = "user_login" ),
    url(r'^logout/',users_view.user_logout, name = "user_logout" ),

    url(r'^cart/(?P<book_id>[0-9]+)/$',cart_view.addToCart, name='cart_page'),
    url(r'^carts/',cart_view.showCart, name='carts'),
    url(r'^remove/(?P<book_id>[0-9]+)/$',cart_view.removeFromCart, name='removeFromCart'),

    # url(r'^ajax_calls/', views.autocompleteModel, name='autocompleteModel'),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
