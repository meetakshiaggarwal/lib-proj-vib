from django.shortcuts import render

# from newsletter.forms import SignUpForm

def home(request):
	# title = "Learing Django"
	# user = "%s" %(request.user)

	# form = SignUpForm(request.POST or None)

	# context = {
	# 	"template_title": title,
	# 	"user_name": user,
	# 	"form": form,
	# }

	# if form.is_valid():
	# 	instance = form.save(commit=False)

	# 	full_name = form.cleaned_data.get("full_name")
	# 	if not full_name:
	# 		full_name = "new new new"

	# 	instance.full_name = full_name

	# 	instance.save()
	# 	context = {
	# 		"template_title": "Thank You",
	# 	}


	return render(request,"home.html",{})
