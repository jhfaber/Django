import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelsTemplates.settings')

import django
django.setup()

## FAKE POPULATE SCRIPT
import random
from ModelTemplatesApp.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fakegen= Faker()
topics = ['Search', 'Social', 'Marketplace','News','Games']
example_emails = ['@gmail.com', '@hotmail.com', '@yahoo.com', '@consofi.com']

def add_topic():
    t = Topic.objects.get_or_create(top_name= random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic
        top = add_topic()

        #create the fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create a fake acces record for that Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]



def populateUsers(N=5):
    for entry in range(N):
        fake_name=fakegen.name()
        fake_last_name =fakegen.name()
        fake_email = fakegen.name() + random.choice(example_emails)

        #Create a  new Users

        user = User.objects.get_or_create(first_name=fake_name,last_name=fake_last_name,email= fake_email)[0]



if __name__ == '__main__':
    print("populating script!")

    populateUsers(20)
    print("populating complete")
