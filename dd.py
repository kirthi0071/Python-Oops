from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    def payment_info(self):
        print("Processing a payment")

class PayPal(PaymentGateway):
    def process_payment(self,amount):
        print(f'Paid {amount} via PayPal')

class RazorPay(PaymentGateway):
    def process_payment(self,amount):
        print(f'Paid {amount} via RazorPay')


pp = PayPal()
rp = RazorPay()

rp.process_payment(1000)
pp.payment_info()
rp.payment_info()
# 4. create PayPal() and RazorPay() objects, call process_payment() and payment_info() on both
pg = PaymentGateway()
