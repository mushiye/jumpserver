# Generated by Django 3.2.14 on 2022-12-28 10:38

import common.db.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0105_auto_20221220_1956'),
        ('tickets', '0025_auto_20221206_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountbackupplanexecution',
            name='plan',
        ),
        migrations.AlterUniqueTogether(
            name='commandfilter',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='commandfilter',
            name='assets',
        ),
        migrations.RemoveField(
            model_name='commandfilter',
            name='nodes',
        ),
        migrations.RemoveField(
            model_name='commandfilter',
            name='user_groups',
        ),
        migrations.RemoveField(
            model_name='commandfilter',
            name='users',
        ),
        migrations.RemoveField(
            model_name='commandfilterrule',
            name='filter',
        ),
        migrations.RemoveField(
            model_name='commandfilterrule',
            name='reviewers',
        ),
        migrations.RemoveField(
            model_name='gathereduser',
            name='asset',
        ),
        migrations.AlterModelOptions(
            name='asset',
            options={'ordering': ['name'],
                     'permissions': [('refresh_assethardwareinfo', 'Can refresh asset hardware info'), ('test_assetconnectivity', 'Can test asset connectivity'), ('push_assetaccount', 'Can push account to asset'), ('test_account', 'Can verify account'), ('match_asset', 'Can match asset'), ('add_assettonode', 'Add asset to node'), ('move_assettonode', 'Move asset to node')], 'verbose_name': 'Asset'},
        ),
        migrations.AlterUniqueTogether(
            name='accountbackupplan',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='accountbackupplan',
            name='recipients',
        ),
        migrations.DeleteModel(
            name='AccountBackupPlanExecution',
        ),
        migrations.DeleteModel(
            name='CommandFilter',
        ),
        migrations.DeleteModel(
            name='CommandFilterRule',
        ),
        migrations.DeleteModel(
            name='GatheredUser',
        ),
        migrations.DeleteModel(
            name='AccountBackupPlan',
        ),
    ]