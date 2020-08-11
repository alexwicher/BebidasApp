from django.contrib.auth.views import PasswordResetView
from django.views.generic import CreateView

from src.account.models import Account
from .forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = '/'
    template_name = '../templates/registration/singup.html'


class PassWordResetCustom(PasswordResetView):
    def form_valid(self, form):
        opts = {
            'use_https': self.request.is_secure(),
            'token_generator': self.token_generator,
            'from_email': self.from_email,
            'email_template_name': self.email_template_name,
            'subject_template_name': self.subject_template_name,
            'request': self.request,
            'html_email_template_name': self.html_email_template_name,
            'extra_email_context': self.extra_email_context,
        }
        if not Account.objects.filter(email=form.data['email']).count() == 1:
            form.add_error('email', 'No account found for that email adress!')
            return super().form_invalid(form)

        form.save(**opts)
        return super().form_valid(form)
