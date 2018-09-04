import account.views
from .forms import SignupForm
from .models import UserProfile
class SignupView(account.views.SignupView):
    
    form_class = SignupForm

    def update_profile(self,form):
        UserProfile.objects.create(
            user=self.created_user,
            College_Name=form.cleaned_data["College_Name"]
        )
    
    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)
