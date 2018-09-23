from django.core.management.base import BaseCommand, CommandError

import dotenv

class Command(BaseCommand):
    help = 'Sets up environment for the client'

    def handle(self, *args, **options):
        API_KEY = input("Enter API KEY: ")
        API_SECRET = input("Enter API SECRET: ")
        with open('.env', 'w') as fp:
            fp.write('')
        dotenv.set_key(dotenv.find_dotenv(), 'API_KEY', API_KEY)
        dotenv.set_key(dotenv.find_dotenv(), 'API_SECRET', API_SECRET)
        self.stdout.write(self.style.SUCCESS('Successfully created .env file'))            