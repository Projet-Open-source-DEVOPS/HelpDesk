#!/usr/bin/python
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Creating 2 users : client and provider"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #Client
        user_client = User.objects.create_user(username='client',
                                    email='client@beatles.com',
                                    password='Test1234')

        
        client_group, created = Group.objects.get_or_create(name='client')
        
        user_client.groups.add(client_group)
        
        #Provider
        user_provider = User.objects.create_user(username='provider',
                                                   email='provider@beat.com',
                                                   password='Test1234')

        provider_group, created = Group.objects.get_or_create(name='provider')

        user_provider.groups.add(provider_group)
        
        user_client.save()
        user_provider.save()