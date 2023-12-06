import pandas as pd
import sqlalchemy as sa
import os
import sys
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Pre-start script'

    def handle(self, *args, **options):
        try:
            csv_data = pd.read_csv('/Users/shelton/Documents/my-class/CSYE7380/CSYE7380/Assignment8/Travel_details_dataset.csv')
            engine = sa.create_engine('mysql+mysqlconnector://root:12345678@localhost:3306/travel_agent')
            csv_data.to_sql('travel_agent', con=engine, if_exists='replace', index=False)
            with open('/Users/shelton/Documents/my-class/CSYE7380/CSYE7380/Assignment8/models.py', 'w') as file:
                sys.stout = file
                call_command('inspectdb')
                sys.stout = sys.__stdout__
                print(sys.stdout)
            call_command('migrate',fake_initial=True)
            print('Done!')
        except Exception as e:
            print(e)
            print('Error while writing models.py')
