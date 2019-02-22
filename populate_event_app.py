import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','nofasol_proj.settings')

import django
django.setup()

from event_app.models import BadgeCategory

def add_badge_categories():
    bc = BadgeCategory.objects.get_or_create(code='VIP',desc='VIP')[0]
    bc.save()
    bc = BadgeCategory.objects.get_or_create(code='Student',desc='Student')[0]
    bc.save()

if __name__ == '__main__':
    print('populating scripts')
    add_badge_categories()
    print('population done')

