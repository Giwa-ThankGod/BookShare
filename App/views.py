from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.core.paginator import Paginator,EmptyPage
from django.contrib import messages
from App.models import *
from App.forms import *
from App.utils import *
from Admin.decorators import *

#Home Page
def index(request):
    globalData = globalVariables()
    categories = globalData['categories']
    newsletter_form = globalData['newsletter_form']
    donate_form = globalData['donate_form']

    try:
        books = Book.objects.all()[:6]
    except:
        books = Book.objects.all()

    cookieData = cookieCart(request)
    cartItems = cookieData['cart_items']
    order = cookieData['order']
    items = cookieData['items']

    context = {
        'categories': categories,
        'books': books,
        'donate_form': donate_form,
        'newsletter_form': newsletter_form,
        'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
        'items': items,
        'order': order,
        'cart_items': cartItems,
    }
    html = ['App/index.html','base.html']
    return render(request, html, context)
#End Home Page

#Category Page
def category(request,category):
    globalData = globalVariables()
    categories = globalData['categories']
    newsletter_form = globalData['newsletter_form']
    donate_form = globalData['donate_form']

    book = Book.objects.filter(category__name=category)

    book_page = Paginator(book, 3)
    #The 3 here represents the number of books per page.

    page_number = request.GET.get('page')
    #Get the page number dynamically from the url ?page = number

    try:
        books = book_page.get_page(page_number)
    except EmptyPage:
        books = book_page.get_page(1)
        
    cookieData = cookieCart(request)
    cartItems = cookieData['cart_items']
    order = cookieData['order']
    items = cookieData['items']

    context = {
        'category': category,
        'categories': categories,
        'books': books,
        'newsletter_form': newsletter_form,
        'donate_form': donate_form,
        'items': items,
        'order': order,
        'cart_items': cartItems,    
    }
    html = ['App/category.html']
    return render(request, html, context)
#End Category Page

#Books Page 
def books(request):
    globalData = globalVariables()
    categories = globalData['categories']
    newsletter_form = globalData['newsletter_form']
    donate_form = globalData['donate_form']

    book = Book.objects.all()

    book_page = Paginator(book, 3)
    #The 3 here represents the number of books per page.

    page_number = request.GET.get('page')
    #Get the page number dynamically from the url ?page = number

    try:
        books = book_page.get_page(page_number)
    except EmptyPage:
        books = book_page.get_page(1)
        
    cookieData = cookieCart(request)
    cartItems = cookieData['cart_items']
    order = cookieData['order']
    items = cookieData['items']
    
    context = {
        'category': category,
        'categories': categories,
        'books': books,
        'newsletter_form': newsletter_form,
        'donate_form': donate_form,
        'items': items,
        'order': order,
        'cart_items': cartItems,
    }
    html = ['App/books.html']
    return render(request, html, context)
#End Books Page

#Cart
def cart(request):
    globalData = globalVariables()
    categories = globalData['categories']
    newsletter_form = globalData['newsletter_form']
    donate_form = globalData['donate_form']

    cookieData = cookieCart(request)
    cartItems = cookieData['cart_items']
    order = cookieData['order']
    items = cookieData['items']

    context = {
        'categories': categories,
        'donate_form': donate_form,
        'newsletter_form': newsletter_form,
        'items': items,
        'order': order,
        'cart_items': cartItems,
    }

    html = ['App/cart.html','base.html']

    return render(request, html, context)
#End Cart

#CheckOut
def checkout(request):
    globalData = globalVariables()
    categories = globalData['categories']
    newsletter_form = globalData['newsletter_form']
    donate_form = globalData['donate_form']

    cookieData = cookieCart(request)
    cartItems = cookieData['cart_items']
    order = cookieData['order']
    items = cookieData['items']

    context = {
        'categories': categories,
        'donate_form': donate_form,
        'newsletter_form': newsletter_form,
        'items': items,
        'order': order,
        'cart_items': cartItems,
    }

    html = ['App/checkout.html','base.html']

    return render(request, html, context)
#End CheckOut

#Donate Logic View
def donate(request):
    if request.method == 'POST':
        donate_form = DonateForm(request.POST)
        if donate_form.is_valid():
            
            #
            body = render_to_string(
                ['App/donate.html','App/admin.html'],
                {
                    'name': request.POST['name'],
                    'email': request.POST['email'],
                    'phone': request.POST['phone'],
                    'value': request.POST['value'],
                    'address': request.POST['address'],
                }
            )
            try:
                send_mail(
                    'Thank you for your Donation',
                    body,
                    request.POST['email']
                )
                send_mail(
                    'New Book Donor',
                    body,
                )
            except:
                return HttpResponse('Error occured')     
    
    return redirect('index') #Redirects the user to the donate section of the index page
#End Donate Logic View

#Newsletter Logic View
def newsletter(request):
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)

        is_email = False
        
        #Checks if the email already exists in our database(Newsletter),
        #if it does then is_email is set true.
        try:
            Newsletter.objects.get(email=request.POST['email'])
            is_email = True
        except:
            pass

        if is_email:
            messages.info(request,'email already registered on our emailing list!!!')
            return redirect('/#newsletter')
        else:
            if newsletter_form.is_valid() or is_email:

                newsletter = Newsletter(
                    email = request.POST['email']
                )
                newsletter.save()

                send_mail(
                    'Greetings from Ebook',
                    'Thank you for signing up to our newsleter\n You will be updated whenever we add a new book',
                    request.POST['email']
                )

                messages.info(request,'Thanks for subscribing to our newsletter!!!')

                return redirect('/#newsletter')

    return redirect('/#newsletter') #Redirects the user to the donate section of the index page
#End Newsletter Logic View

#Contact Page
def contact(request):
    globalData = globalVariables()
    categories = globalData['categories']
    newsletter_form = globalData['newsletter_form']
    donate_form = globalData['donate_form']

    cookieData = cookieCart(request)
    cartItems = cookieData['cart_items']
    order = cookieData['order']
    items = cookieData['items']

    context = {
        'categories': categories,
        'donate_form': donate_form,
        'newsletter_form': newsletter_form,
        'items': items,
        'order': order,
        'cart_items': cartItems,
    }
    html = ['App/contact.html','base.html']

    return render(request, html, context)
#End Contact Page
