
from .models import Department
from django.db.models import F

def cleaning(input_val=''):
    input_val = input_val.replace('ي', 'ی').strip()
    return input_val

for rec in Department.objects.all():
    rec.dep_title = cleaning(rec.dep_title)
    rec.save()

