from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, redirect


def sub(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("***_****_**************", "************************"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'index1.html')


@ csrf_exempt
def success(request):
    return render(request, "services.html")


@ csrf_exempt
def service(request):
    return redirect("ocr/templates/services.html")
