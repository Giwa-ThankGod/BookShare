from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, redirect, render
from Paystack.forms import PaymentForm
from Paystack.models import *
from App.utils import *

def initiate_payment(request: HttpResponse) -> HttpResponse:

    globalData = globalVariables()
    categories = globalData['categories']
    newsletter_form = globalData['newsletter_form']
    donate_form = globalData['donate_form']
    
    cookieData = cookieCart(request)
    cartItems = cookieData['cart_items']
    order = cookieData['order']
    items = cookieData['items']

    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if not payment_form.is_valid():

            payment = Payment(
                amount = order['get_cart_total'],
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                shipping_address = request.POST['shipping_address'],
                phone = request.POST['phone'],
            )
            payment.save()

            admin = render_to_string(
                'payment/checkout.html',
                {
                    'payment': payment,
                }
            )
            recepient = render_to_string(
                'payment/recepient.html',
                {
                    'payment': payment,
                    'items': items,
                    'cartItems': cartItems,
                }
            )
            try:
                send_mail(
                    'New Purchase',
                    admin,
                )
                send_mail(
                    'Ebook Purchase Reciept',
                    recepient,
                    request.POST['email']
                )
            except:
                pass

            html = ['payment/make_payment.html','base.html']

            return render(
                request, 
                html, 
                {
                    'payment': payment, 
                    'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
                    'categories': categories,
                    'newsletter_form': newsletter_form,
                    'donate_form': donate_form,
                    'order': order,
                    'cart_items': cartItems,
                },
            )
        else:
            print('Form not valid!')
    else:
        payment_form = PaymentForm()

        html = ['payment/initiate_payment.html','base.html']

        context = {
            'payment_form': payment_form,
            'categories': categories,
            'newsletter_form': newsletter_form,
            'donate_form': donate_form,
            'items': items,
            'order': order,
            'cart_items': cartItems,
        }

        return render(request, html, context)

def verify_payment(request: HttpResponse, ref) -> HttpResponse:
    payment = get_object_or_404(Payment, ref = ref)
    verified = payment.verify_payment()
    
    return redirect('initiate-payment')


