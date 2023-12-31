# Generated by Django 4.1.7 on 2023-11-21 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0002_recur_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='cust_comments',
            fields=[
                ('commentid', models.AutoField(primary_key=True, serialize=False, verbose_name='COMMENTID')),
                ('comment', models.CharField(max_length=250, null=True)),
                ('custcom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.recurring_invoice')),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
