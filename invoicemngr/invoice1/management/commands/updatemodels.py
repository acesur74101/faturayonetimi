from typing import Any, Optional
from django.core.management.base import BaseCommand

import pandas as pd
import invoice1.models
class Command(BaseCommand):
    help = 'import booms'


    def add_arguments(self, parser):
        pass
    def handle(self, *args, **options):
        
       df = pd.read_csv("country22.csv",delimiter=';')
       for name1, code1 ,iso1 in zip(df.COUNTRY,df.CODE,df.ISO):
           model=invoice1.models.Country(name=name1,code=code1,iso=iso1)
           model.save()
       