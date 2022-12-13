# from django.urls import path
# from  accounts import views as user_view
# from django.contrib.auth import views as auth_views,tokens

# urlpatterns = [
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('logout/', auth_views.logout_then_login, name='logout'),
#     path('register/',user_view.register,name='register'),
#     path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
#     path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
#     path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset/'),
#     path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
#     path('reset/<uidb64>/<token>/',tokens.PasswordResetTokenGenerator.key_salt())

# ]

from .views import RegistrationView, UsernameValidationView, EmailValidationView, LogoutView, VerificationView, LoginView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
         name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name='validate_email'),
    path('activate/<uidb64>/<token>',
         VerificationView.as_view(), name='activate'),
]