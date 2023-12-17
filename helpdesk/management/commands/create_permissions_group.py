#!/usr/bin/python
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Add the correct permissions in right group"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Set client permission
        codenames_client = ['user_can_view_own_tickets']

        client_permissions = Permission.objects.filter(codename__in=codenames_client)
        client_group, created = Group.objects.get_or_create(name='client')
        client_group.permissions.set(client_permissions)

        # Set provider permission
        codenames_provider = ['user_can_view_tickets_where_assigned','user_can_view_all_tickets_not_assigned']

        provider_permissions = Permission.objects.filter(codename__in=codenames_provider)
        provider_group, created = Group.objects.get_or_create(name='provider')
        provider_group.permissions.set(provider_permissions)
