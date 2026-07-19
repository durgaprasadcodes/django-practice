from django.shortcuts import render

def shop(request):
    return render(request,'shop.html')

def shop_details(request):
    return render(request,'shop_details.html')