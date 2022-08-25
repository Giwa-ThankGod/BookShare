import json
from django.core.mail import EmailMessage
from django.conf import settings
from App.models import *
from App.forms import *

def globalVariables():
    categories = Category.objects.all()
    newsletter_form = NewsletterForm()
    donate_form = DonateForm()

    return {
        'categories': categories,
        'donate_form': donate_form,
        'newsletter_form': newsletter_form,
    }

# Mailing function
def send_mail(subject,body,recepient = settings.EMAIL_HOST_USER):
    email = EmailMessage(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [recepient],
    )
    email.fail_silently=False
    email.send()
#End Mailing function

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print(cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']

            book = Book.objects.get(id=i)
            total = (book.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'book': {
                    'id': book.id,
                    'title': book.title,
                    'description': book.description,
                    'price': book.price,
                    'ref': book.ref,
                    'cover': book.cover,
                    'category': book.category,
                    'author': book.author,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total,
            }

            items.append(item)

        except:
            pass
        
    return {'items': items,'order': order,'cart_items': cartItems,}