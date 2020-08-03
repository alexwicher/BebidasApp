from django.contrib.auth import views as auth_views
from django.urls import path, include

from src.account.views import SignUpView, PassWordResetCustom

app_name = 'account'
templatePath = '../templates/registration/passwordReset/'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path(
        'password_reset/',
        PassWordResetCustom.as_view(template_name=templatePath + 'password_reset.html',
                                    subject_template_name=templatePath + 'password_reset_subject.txt',
                                    email_template_name=templatePath + 'password_reset_email.html',
                                    success_url='done/'
                                    )
    ),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name=templatePath + 'password_reset_confirm.html',
             success_url='../../done/'
         )
         ),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name=templatePath + 'password_reset_complete.html'
         )
         ),
    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name=templatePath + 'password_reset_done.html'
         )
         ),
    path('', include('django.contrib.auth.urls')),  # keep at the end ...

]
# account/login/ [name='login']
# account/logout/ [name='logout']
# account/password_change/ [name='password_change']
# account/password_change/done/ [name='password_change_done']
# account/password_reset/ [name='password_reset']
# account/password_reset/done/ [name='password_reset_done']
# account/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# account/reset/done/ [name='password_reset_complete']
