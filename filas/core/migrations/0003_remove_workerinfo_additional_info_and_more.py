# Generated by Django 4.2.7 on 2023-11-24 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_workerinfo_additional_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workerinfo',
            name='additional_info',
        ),
        migrations.RemoveField(
            model_name='workerinfo',
            name='task_status',
        ),
        migrations.AddField(
            model_name='workerinfo',
            name='request_host_external_ip_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workerinfo',
            name='request_host_internal_ip_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workerinfo',
            name='task_host_external_ip_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workerinfo',
            name='task_host_internal_ip_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
