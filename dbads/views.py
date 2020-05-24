from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

def dbadspage(request):
  template_name = 'dbadspage.html'
  return render(request, template_name, {})
