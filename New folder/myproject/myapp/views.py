from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def your_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User(username=username, password=password)
            user.save()
            return redirect('your_view')
    else:
        form = UserForm()
    
    data = User.objects.all()
    return render(request, 'index.html', {'data': data, 'form': form})


from .models import AdminUser
from .forms import AdminLoginForm


def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            admin_user = AdminUser(username=username, password=password)
            admin_user.save()
            return redirect('admin_login')  # Redirect to the same page after successful login
    else:
        form = AdminLoginForm()
    
    return render(request, 'admin_login.html', {'form': form})