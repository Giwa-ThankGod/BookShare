from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Admin.decorators import *
from Admin.forms import *
from Admin.models import *
from Admin.utils import *
from App.models import *
from django.conf import settings

''' ADMIN PAGE VIEWS AND LOGIC '''

@login_required(login_url = 'login')
@authenticated_user
def admin_index(request):
    author = Author.objects.all()
    book = Book.objects.all()
    category = Category.objects.all()
    newsletter = Newsletter.objects.all()

    notificationData = notification()
    recent_activity = notificationData['recent_activity']
    alert_activity = notificationData['alert_activity']

    context = {
        'author': author,
        'book': book,
        'category': category,
        'newsletter': newsletter,
        'recent_activity': recent_activity,
        'alert_activity': alert_activity,
    }

    html = ['admin_base.html','admin_base.html']
    return render(request, 'Admin/index.html', context)

@login_required(login_url = 'login')
def authors(request):
    author = Author.objects.all()

    notificationData = notification()
    recent_activity = notificationData['recent_activity']
    alert_activity = notificationData['alert_activity']

    context = {
        'author': author,
        'recent_activity': recent_activity,
        'alert_activity': alert_activity,
    }
    html = ['Admin/author.html','admin_base.html']

    return render(request, html, context)

@login_required(login_url = 'login')
def add_authors(request):

    notificationData = notification()
    recent_activity = notificationData['recent_activity']
    alert_activity = notificationData['alert_activity']

    author_form = AuthorForm()
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()

            # author_instance = Author.objects.create(
            #     name = request.POST["name"]
            # )
            # author_instance.save()
            #Creates a new author instance

            messages.success(request, 'author was added successfully!!!')
            return redirect('admin-authors')

    context = {
        'author_form': author_form,
        'recent_activity': recent_activity,
        'alert_activity': alert_activity,
    }
    html = ['Admin/author_form.html','admin_base.html']

    return render(request, html, context)

@login_required(login_url = 'login')
def edit_authors(request, id):
    author_instance = Author.objects.get(id=id)

    author_form = AuthorForm(instance = author_instance)

    notificationData = notification()
    recent_activity = notificationData['recent_activity']
    alert_activity = notificationData['alert_activity']
    
    if request.method == 'POST':
        author_form = AuthorForm(request.POST, instance = author_instance)
        if author_form.is_valid():
            author_form.save()

            # author_instance = Author.objects.create(
            #     name = request.POST["name"]
            # )
            # author_instance.save()
            #Creates a new author instance

            messages.success(request, 'author was edited successfully!!!')
            return redirect('admin-authors')

    context = {
        'author_form': author_form,
        'recent_activity': recent_activity,
        'alert_activity': alert_activity,
    }
    html = ['Admin/author_form.html','admin_base.html']

    return render(request, html, context)

@login_required(login_url = 'login')
def delete_authors(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        messages.success(request, 'author was deleted successfully!!!')
    except:
        messages.error(request ,'An error occured \n Author with name {id} does not exist')
    return redirect('admin-authors')

@login_required(login_url = 'login')
def books(request):
    book = Book.objects.all()

    notificationData = notification()
    recent_activity = notificationData['recent_activity']
    alert_activity = notificationData['alert_activity']

    context = {
        'book': book,
        'recent_activity': recent_activity,
        'alert_activity': alert_activity,
    }
    html = ['Admin/book.html','admin_base.html']

    return render(request, html, context)

@login_required(login_url = 'login')
def add_books(request):
    author = Author.objects.all()
    category = Category.objects.all()

    notificationData = notification()
    recent_activity = notificationData['recent_activity']
    alert_activity = notificationData['alert_activity']

    book = BookForm()
    if request.method == 'POST':
        book = BookForm(request.POST, request.FILES)
        if book.is_valid() or True:
            #author instance to be assigned to Book Model
            author_instance = Author.objects.get(name=request.POST['author'])
            
            books = Book(
                title = book.cleaned_data['title'],
                description = book.cleaned_data['description'],
                price = book.cleaned_data['price'],
                cover = book.cleaned_data['cover'],
                author = author_instance,
            )
            books.save()
            
            for i in request.POST.getlist('category'): #Gets all selected item from html form.
                category = Category.objects.get(id = int(i))
                books.category.add(category)
                
            # print(request.POST.getlist('category'))
            messages.success(request, 'book was added successfully!!!')
            return redirect('admin-books')
        else:
            messages.error(request, 'form is invalid!!!')

    context = {
        'author': author,
        'category': category,
        'book_form': book,
        'recent_activity': recent_activity,
        'alert_activity': alert_activity,
    }
    html = ['Admin/book_form.html','admin_base.html']

    return render(request, html, context)

@login_required(login_url = 'login')
def edit_books(request, id):
    author = Author.objects.all()
    category = Category.objects.all()

    book_instance = Book.objects.get(id=id)

    notificationData = notification()
    recent_activity = notificationData['recent_activity']
    alert_activity = notificationData['alert_activity']
    
    book = BookForm(instance = book_instance)
    if request.method == 'POST':
        print(request.POST)
        book = BookForm(
            request.POST,
            request.FILES,
            instance = book_instance,
        )
        if book.is_valid():
            book.save()
                
            messages.success(request, 'book was edited successfully!!!')
            return redirect('admin-books')
        else:
            messages.error(request, 'form is invalid!!!')
            return redirect('admin-books')

    context = {
        'author': author,
        'category': category,
        'book_form': book,
        'book_instance': book_instance,
        'recent_activity': recent_activity,
        'alert_activity': alert_activity,
    }
    html = ['Admin/edit_book_form.html','admin_base.html']

    return render(request, html, context)

@login_required(login_url = 'login')
def delete_books(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        messages.success(request, 'book was deleted successfully!!!')
    except:
        messages.error(request ,'An error occured \n Book with name {id} does not exist')
    return redirect('admin-books')

@login_required(login_url = 'login')
def categorys(request):
    category = Category.objects.all()

    notificationData = notification()
    recent_activity = notificationData['recent_activity']
    alert_activity = notificationData['alert_activity']

    context = {
        'category': category,
        'recent_activity': recent_activity,
        'alert_activity': alert_activity,
    }
    html = ['Admin/category.html','admin_base.html']

    return render(request, html, context)

@login_required(login_url = 'login')
def add_categorys(request):

    notificationData = notification()
    recent_activity = notificationData['recent_activity']
    alert_activity = notificationData['alert_activity']

    category = CategoryForm(request.POST, request.FILES)
    if request.method == 'POST':
        category = CategoryForm(request.POST, request.FILES)
        if category.is_valid():
            category.save()
            # category_instance = Category(
            #     name = category.cleaned_data['name'],
            #     thumb = category.cleaned_data['thumb'],
            # )
            # category_instance.save()
            #Creates a new author instance

            messages.success(request, 'category was added successfully!!!')
            return redirect('admin-categorys')

    context = {
        'category_form': category,
        'recent_activity': recent_activity,
        'alert_activity': alert_activity,
    }
    html = ['Admin/category_form.html','admin_base.html']

    return render(request, html, context)

@login_required(login_url = 'login')
def edit_categorys(request, id):

    category = Category.objects.get(id=id)

    notificationData = notification()
    recent_activity = notificationData['recent_activity']
    alert_activity = notificationData['alert_activity']

    category_form = CategoryForm(instance=category)
    if request.method == 'POST':
        category_form = CategoryForm(request.POST, request.FILES, instance=category)
        if category_form.is_valid():
            category_form.save()

            # category = Category(
            #     instance=category,
            #     name = category_form.cleaned_data['name'],
            #     thumb = category_form.cleaned_data['thumb'],
            # )
            # category.save()
            #Creates a new author instance

            messages.success(request, 'category was edited successfully!!!')
            return redirect('admin-categorys')

    context = {
        'category_form': category_form,
        'recent_activity': recent_activity,
        'alert_activity': alert_activity,
    }
    html = ['Admin/category_form.html','admin_base.html']
    return render(request, html, context)

@login_required(login_url = 'login')
def delete_categorys(request, id):
    try:
        category = Category.objects.get(id=id)
        category.delete()
        messages.success(request, 'category was added successfully!!!')
    except:
        messages.error(request ,'An error occured \n * Category with name {id} does not exist')
    return redirect('admin-categorys')

@login_required(login_url = 'login')
def newsletter(request):

    newsletter = Newsletter.objects.all()

    notificationData = notification()
    recent_activity = notificationData['recent_activity']
    alert_activity = notificationData['alert_activity']

    context = {
        'newsletter': newsletter,
        'recent_activity': recent_activity,
        'alert_activity': alert_activity,
    }
    html = ['Admin/newsletter.html','admin_base.html']

    return render(request, html, context)

@login_required(login_url = 'login')
def delete_newsletters(request, id):
    try:
        newsletter = Newsletter.objects.get(id=id)
        newsletter.delete()
        messages.success(request, 'newsletter was added successfully!!!')
    except:
        messages.error(request ,'An error occured \n * newsletter with name {id} does not exist')
    return redirect('admin-newsletter')

# def logout(request):
    
#     return render(request, 'registration/logout_page.html')


