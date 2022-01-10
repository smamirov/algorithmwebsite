from django.shortcuts import render

# Home Page View
def home_page(request):
    return render(request, 'home.html')
