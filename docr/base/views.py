from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt


def sub(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_test_QcFK6enY6yUXQ7", "yqvmoWDoFQAIIzdCRGD9z6nM"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'index1.html')


@ csrf_exempt
def success(request):
    return render(request, "success.html")
