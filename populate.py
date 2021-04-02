import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'mysite.settings')

import django
django.setup()
from scishare.models import Category, Study, Group
def populate():

    cats = {}

    for cat, cat_data in cats.items():
        c = add_cat(cat,up_votes=cat_data['up_votes'],down_votes=cat_data['down_votes'])
        for p in cat_data['pages']:
            add_study(c, p['title'], p['url'])
            add_study(c,p['title'],p['url'],up_votes=p['up_votes'])

    for c in Category.objects.all():
        for p in Study.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_study(cat, title, url, up_votes=0,down_votes=0):
    p = Study.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.up_votes = up_votes
    p.down_votes = down_votes
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_group(group_name):
    g = Group.objects.get_or_create(group_name=group_name)[0]
    g.save()
    return g

if __name__ == '__main__':
    print('Starting WAD population script...')
    populate()