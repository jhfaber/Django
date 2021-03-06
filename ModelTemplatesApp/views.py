from django.shortcuts import render
from ModelTemplatesApp.models import AccessRecord, User
from . import forms

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    #my_dict = {'insert_content': "HELLO I AM FROM MODELTEMPLATEAPP"}
    return render (request, 'ModelTemplatesApp/index.html', context=date_dict)

def help(request):
    my_dict = {'insert_content': "I DON'T HELP ANYBODY"}
    return render (request, 'ModelTemplatesApp/index.html', context=my_dict)

def users(request):
    users_list = User.objects.order_by('first_name')
    my_users = {'users':users_list}
    return render (request, 'ModelTemplatesApp/users.html', context=my_users)

def form_name_view(request):
    form= forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING CODE
            print("VALIDATION SUCCESS")
            print("NAME: "+ form.cleaned_data['name'])
            print("EMAIL: "+ form.cleaned_data['email'])
            print("TEXT: "+ form.cleaned_data['text'])

    return render(request, 'ModelTemplatesApp/form_page.html',{'form':form})
