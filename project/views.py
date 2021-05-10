from django.shortcuts import render

def HomeView(request):
    return render(request,'pages/home.html')

def AboutView(request):
    return render(request,'pages/about.html')

def ContactView(request):
    return render(request,'pages/contact.html')

def ServicesView(request):
    return render(request,'pages/services.html')



def handler404(request, exeption):
    return render(request,'errors/404.html', {}, status=404)