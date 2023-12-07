# Generated by Django 5.0 on 2023-12-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0038_checklist_checklisttemplate_checklisttask'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('user_can_view_all_tickets', 'User can view all tickets'), ('user_can_view_own_tickets', 'User can view own tickets'), ('user_can_view_tickets_where_assigned', 'User can view the tickets where he is assigned.')),
            },
        ),
    ]
