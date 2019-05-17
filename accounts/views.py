from django.shortcuts import render
# IMPORT DJANGO AUTH
from django.contrib import auth
# IMPORT DJANGO USER MODEL
# Prebuilt standard user model
from django.contrib.auth.models import User 

# Create your views here.
# Register
def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check if username exists
      if User.objects.filter(username=username).exists():
        return render(request, 'accounts/register.html', {'error': 'That username has already been registered. Please try a different username'})
      else:
        # Check if email exists
        if User.objects.filter(email=email).exists():
          return render(request, 'accounts/register.html', {'error': 'That email has already been registered'})
        else:
          # Register User
          ## Uses bcrypt for the password
          user = User.objects.create_user( 
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          user.save()
          return redirect('login')
    else:
      return render(request, 'accounts/register.html', {'error': 'Passwords do not match'})
  else:
    return render(request, 'accounts/register.html')