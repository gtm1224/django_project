from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login
from .forms import LoginForm, RegistrationForm, UserProfileForm, UserForm,UserInfoForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile,UserInfo
from django.contrib.auth.models import User
def user_login(request):
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request,'account/login.html',{'form':login_form})
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse('Welcome. You have logged in')
            else:
                return HttpResponse('Sorry, your username or password is not right.')
        else:
            return HttpResponse('Invalid login')



def register(request):
    if request.method == 'GET':
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, 'account/register.html',{'form':user_form,'profile':userprofile_form})
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse('Congratulations! You have successfully registered.')
        else:
            return HttpResponse('Sorry. Something went wrong, please try again.')


@login_required()
def myself(request):
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user,
    'userprofile') else UserProfile.objects.create(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user,'userinfo') else UserInfo.objects.create(user=request.user)
    return render(request,"account/myself.html",{"user":request.user,"userinfo":userinfo,"userprofile":userprofile})


@login_required()
def myself_edit(request):
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user,'userprofile') else UserProfile.objects.create(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user,'userinfo') else UserInfo.objects.create(user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST)
        userprofile_form=UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            request.user.email = user_cd['email']
            userprofile.phone = userprofile_cd['phone']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.aboutme = userinfo_cd['aboutme']
            request.user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/aboutme/')
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"phone":userprofile.phone})
        userinfo_form = UserInfoForm(initial={"company":userinfo.company,"profession":userinfo.profession,"aboutme":userinfo.aboutme})
        return render(request,"account/myself_edit.html",{"user_form":user_form,"userprofile_form":userprofile_form,"userinfo_form":userinfo_form})

@login_required()
def my_image(request):
    if request.method == 'POST':
        img = request.POST['img']
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse('1')
    return render(request,'account/imagecrop.html',)