from django import forms
from django.http import HttpResponse
from django.shortcuts import render

from myapp import models


class LoginForm(forms.Form):
    username=forms.CharField(label="用户名",
                             widget=forms.TextInput(attrs={"class":"form-control"}))

    password=forms.CharField(label="密码"
                             ,widget=forms.PasswordInput(attrs={"class":"form-control"}))
def load(request):
    if request.method=='GET':
        form=LoginForm()
        return render(request,'load.html',{'form':form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        #获取了用户名和密码
        print(form.cleaned_data)
        user_obj=models.UserInfo.objects.filter(name=form.cleaned_data['username'],
                                                password=form.cleaned_data['password']).first()
        if not user_obj:
            form.add_error("password","用户名或密码错误")
            return render(request, 'load.html', {'form': form})
        #return HttpResponse("提交成功")
        request.session["info"]={'id':user_obj.name};

        return render(request,'locate.html',{'current_user':request.session["info"]['id'] })
    return render(request,'load.html',{'form':form})

def logout(request):
    request.session.clear()
    return HttpResponse('注销成功')