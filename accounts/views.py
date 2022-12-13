
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate,  login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .forms import UserCreationForm
# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template
# from .forms import LoginForm

# def login_page(request):
#     forms = LoginForm()
#     if request.method == 'POST':
#         forms = LoginForm(request.POST)
#         if forms.is_valid():
#             username = forms.cleaned_data['username']
#             password = forms.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('dashboard')
#     context = {'form': forms}
#     return render(request, 'users/login.html', context)
# #

# def register(request):
#     if request.method=='POST':
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data.get('username')
#             email=form.cleaned_data.get('email')
#             ########## email System
#             htmly=get_template('users/email.html')
#             context={'username':username}
#             subject,from_email,to='Welcome ','your_email@gmail.com', email
#             html_context=htmly.render(context)
#             msg=EmailMultiAlternatives(subject,html_context,from_email,[to])
#             msg.attach_alternative(html_context,'txt/html')
#             msg.send()
#             messages.success(request,'Your Account Has Been Created')
#             redirect('login')
#         else:
#             form=UserCreationForm()
#         return render(request,'users/register',{'form':form,'title':'register here'})



# def logout_page(request):
#     logout(request)
#     return redirect('login')
