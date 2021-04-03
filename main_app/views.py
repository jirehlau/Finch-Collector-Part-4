from django.shortcuts import render, redirect
from .models import Restaurant

# Create your views here.
# Add the following import
from django.http import HttpResponse

def delete(request, r_id):
  # find the cat with this id in the database and delete it
  r = Restaurant.objects.get(id=r_id)
  r.delete()
  return redirect('/restaurants')

# FORM CREATION 
def create_form(request):
  return render(request,'create_form.html')

# create part 2 - handle the form submission 
def submit_create_form(request):
  # put form data in database 
  Restaurant.objects.create(
    name = request.POST['name'],
    description=request.POST['description'],
    cuisine=request.POST['cuisine'],
    capacity=request.POST['capacity'],
  )
  return redirect('/restaurants')

# FORM EDITS 
def edit_form(request, r_id):
  r = Restaurant.objects.get(id=r_id)
  return render(request, 'edit_form.html', {'r': r,})

def submit_update_form(request, r_id):
  this_r = Restaurant.objects.get(id=r_id)
  this_r.name = request.POST['name']
  this_r.cuisine = request.POST['cuisine']
  this_r.description = request.POST['description']
  this_r.capacity= request.POST['capacity']
  this_r.save()  
  return redirect('/restaurants')

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def restaurants_index(request):
    restaurants = Restaurant.objects.all()
    return render(request,'restaurants/index.html',{'restaurants': restaurants})

def restaurants_detail(request, r_id):
  r = Restaurant.objects.get(id=r_id)
  return render(request, 'restaurants/detail.html', { 'r': r })