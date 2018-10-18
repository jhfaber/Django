from django.shortcuts import render
from ModelTemplatesApp.models import AccessRecord

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
    my_users = {}
