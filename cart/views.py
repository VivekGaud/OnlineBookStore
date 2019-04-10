from django.shortcuts import render, redirect
from books.models import book_category,book_details
from .models import cart_details
from django.contrib import messages
import pdb 

# Create your views here.
def addToCart(request,book_id):
	# Adding books to cart
	print(book_id)
	prod = book_details.objects.filter(id=book_id)
	print(prod)
	for i in prod:
		book_ID=i.id
		book_cat = i.book_cat
		auther_name = i.auther_name
		book_price = i.book_price
		book_img = i.book_img
		book_pdf = i.book_pdf
	print(book_img)
	user_name = request.session['username']
	_, cartDetails = cart_details.objects.get_or_create(
				book_id=book_ID,
                user_name=user_name,
                auther_names=auther_name,
                book_prices=book_price,
                book_img=book_img,
                quantity=0
                )
	messages.info(request,f"{ auther_name } book added to cart")
	return redirect("index")


def showCart(request):
	
	if request.session._session:
		sessionReq = request.session['username']
		name = str(sessionReq)
		uName = cart_details.objects.filter(user_name=sessionReq)
		count_cart_book = cart_details.objects.filter(user_name=sessionReq).count()
	else:
		sessionReq = "zzz"
	all_book = book_details.objects.all()
	context = {
	'sessionReq':sessionReq,
	'uName':uName,
	'name':name,
	'all_book':all_book,
	'count_cart_book':count_cart_book,
	}
	return render(request, 'cart/cart_page.html',context)

def removeFromCart(request,book_id):
	removedItem = cart_details.objects.filter(book_id=book_id)
	for i in removedItem:
		name=i.auther_names
	removedItem.delete()
	messages.info(request,f"{ name } is removed from cart")
	return redirect("carts")
