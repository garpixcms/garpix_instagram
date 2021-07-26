from django.core.management.base import BaseCommand
from ...instagram import Instagram
import time


class Command(BaseCommand):
    help = 'get instagram data'

    def handle(self, *args, **kwargs):
        while True:
            print('start get instagram data')
            start_time = time.time()
            inst = Instagram()
            inst.update_base()
            print('end get instagram data')
            print('wait 20 minutes until the next iteration')
            print(f'it takes a {time.time() - start_time} sec')
            time.sleep(1200)
