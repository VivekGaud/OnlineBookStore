from django.shortcuts import render, redirect
from .models import book_category,book_details
from django.http import Http404,HttpResponse
from django.contrib import messages
from cart.models import cart_details
import pdb 



def index(request):
    all_book = book_details.objects.all()
    all_cat = book_category.objects.all()
    count= book_details.objects.all().count()
    if request.session._session:
        sessionReq = request.session['username']
        count_cart_book = cart_details.objects.filter(user_name=sessionReq).count()
    else:
        count_cart_book =0
        sessionReq = "zzz"
    print("total book in cart",count_cart_book)
    context = {
    'all_book':all_book,   
    'all_cat':all_cat,
    'count':count,
    'sessionReq':sessionReq,
    'count_cart_book':count_cart_book,
    }
    return render(request,'books/shop.html',context)

def detail(request, book_id):
    try:
        book = book_details.objects.get(pk=book_id)
        if request.session._session:
            sessionReq = request.session['username']
            count_cart_book = cart_details.objects.filter(user_name=sessionReq).count()
        else:
            count_cart_book =0
            sessionReq = "zzz"
        
    except book_details.DoesNotExist:
        raise Http404("Book Does Not Exist")
    all_book = book_details.objects.all()
    context={
    'count_cart_book':count_cart_book,
    'book':book,'sessionReq':sessionReq,'all_book':all_book,
    }
    return render(request, 'books/single-product-details.html', context)

def cat_detail(request, cat_id):
    count =0
    try:
        book_catego = book_category.objects.get(pk=cat_id)
        all_book = book_details.objects.all()
        all_cat = book_category.objects.all()
        print(book_catego)
        for i in range(all_book.count()):
        	print(all_book[i].book_cat)
        	if all_book[i].book_cat == book_catego:
        		count +=1
        
        if request.session._session:
            sessionReq = request.session['username']
            count_cart_book = cart_details.objects.filter(user_name=sessionReq).count()
        else:
            count_cart_book=0
            sessionReq = "zzz"
        
        # print(all_book[1].book_cat)
        print(sessionReq)
        context={
        'book_catego':book_catego,
        'all_book':all_book,
        'all_cat':all_cat,
        'count':count,
        'sessionReq':sessionReq,
        'count_cart_book':count_cart_book,
        }
    except book_category.DoesNotExist:
        raise Http404("Book Does Not Exist")
    return render(request, 'books/cat_page.html', context)

def search_bar(request):
    query = request.GET.get('search')
    print(query,"search_text")
    search_res = book_details.objects.filter(book_name=query)
    book_name="defaultName"

    print(search_res)
    for i in search_res:
        book_id=i.id
        book_name=i.book_name
    
    if book_name==str(query):
        book = book_details.objects.get(pk=book_id)
        
    else:
        messages.info(request,f"{ query } is not avilable ")
        return redirect("homepage")
    if request.session._session:
        sessionReq = request.session['username']
        count_cart_book = cart_details.objects.filter(user_name=sessionReq).count()
        
    else:
        count_cart_book=0
        sessionReq = "zzz"
    all_book = book_details.objects.all()  
    context={
    'book':book,
    'sessionReq':sessionReq,
    'all_book':all_book,
    'count_cart_book':count_cart_book,
    }
    return render(request, 'books/single-product-details.html', context)


