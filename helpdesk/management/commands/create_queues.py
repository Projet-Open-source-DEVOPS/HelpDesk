#!/usr/bin/python
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User

from helpdesk.models import Queue


class Command(BaseCommand):
    help = "Creating 2 queue : incident and demande"

    def add_arguments(self, parser):
        pass
    
    
    def handle(self, *args, **options):
        queue_data = [
        {"model": "helpdesk.queue", "pk": 1, "fields": {"title": "Ticket Demande", "slug": "TD", "email_address": "django-helpdesk@example.com", "locale": "en-US", "allow_public_submission": True, "allow_email_submission": True, "escalate_days": 5, "new_ticket_cc": "", "updated_ticket_cc": "", "email_box_type": None, "email_box_host": "", "email_box_port": None, "email_box_ssl": False, "email_box_user": "", "email_box_pass": "", "email_box_imap_folder": "", "email_box_local_dir": "", "permission_name": "helpdesk.queue_access_TD", "email_box_interval": 5, "email_box_last_check": None, "socks_proxy_type": None, "socks_proxy_host": None, "socks_proxy_port": None, "logging_type": None, "logging_dir": "", "default_owner": None}},
        {"model": "helpdesk.queue", "pk": 2, "fields": {"title": "Ticket Incident", "slug": "TI", "email_address": "sp-help@example.com", "locale": "en-US", "allow_public_submission": True, "allow_email_submission": True, "escalate_days": None, "new_ticket_cc": "", "updated_ticket_cc": "", "email_box_type": None, "email_box_host": "", "email_box_port": None, "email_box_ssl": False, "email_box_user": "", "email_box_pass": "", "email_box_imap_folder": "", "email_box_local_dir": "", "permission_name": "helpdesk.queue_access_TI", "email_box_interval": 5, "email_box_last_check": None, "socks_proxy_type": None, "socks_proxy_host": None, "socks_proxy_port": None, "logging_type": None, "logging_dir": "", "default_owner": None}}
        ]

        for queue_info in queue_data:
            queue_fields = queue_info.get("fields", {})
            Queue.objects.update_or_create(pk=queue_info["pk"], defaults=queue_fields)


    