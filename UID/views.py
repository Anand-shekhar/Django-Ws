from django.shortcuts import render
from .forms import LogInForm
# Create your views here.
def logins(request):
	if request.method == "POST":
		pass
	else:
		pass
			forms = LogInForm()
			return render(request, 'user/Authlogin.html',{
					'form':form
				})