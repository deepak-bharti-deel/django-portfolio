from django.shortcuts import render

# Create your views here.

def wish_shakti(request):
  template = 'shakti/wish_shakti.html'
  context = {}
  return render(request, template, context)