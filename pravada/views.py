from django.shortcuts import render

def error_404(request):
    return render(request, '404.html')

def error_500(request):
    return render(request, '500.html')