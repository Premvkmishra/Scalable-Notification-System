from django.shortcuts import render

# Define a home view
def home(request):
    return render(request, 'index.html')  # Ensure you have an 'index.html' file in your templates folder
