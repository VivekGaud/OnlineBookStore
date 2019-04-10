from django.shortcuts import render
from django.db.models import Max
from books.models import book_category,book_details
from cart.models import cart_details
import random

def index(request):
	all_book = book_details.objects.all()
	all_cat = book_category.objects.all()
	if request.session._session:
		sessionReq = request.session['username']
		count_cart_book = cart_details.objects.filter(user_name=sessionReq).count()
	else:
		sessionReq = "zzz"
		count_cart_book =0
	random_items = random.sample(list(all_book), 3)
	random_items_cat = random.sample(list(all_cat), 3)
	random_single_item = random.choice(all_book)
	print(random_items_cat)
	context = {
	'random_items':random_items,
	'random_items_cat':random_items_cat,
	'random_single_item':random_single_item,
	'all_book':all_book,
	'count_cart_book':count_cart_book,
	}
	return render(request,'books/home.html',context)