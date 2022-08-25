from django.db import models
from Paystack.paystack import Paystack
import secrets # This is a django module that helps generate a unique token number

class Payment(models.Model):
    amount = models.PositiveIntegerField(default=100)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    shipping_address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f"Payment: {self.amount}"

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50) #50 is the length of the ref
            object_with_similar_ref = Payment.objects.filter(ref = ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    def amount_value(self) -> int:
        return self.amount * 100

    def verify_payment(self):
        paystack = Paystack()
        status , result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False

    

