# Generated by Django 3.1.6 on 2021-02-13 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.TextField(blank=True, null=True)),
                ('refresh_token', models.CharField(blank=True, max_length=300, null=True)),
                ('token_type', models.CharField(blank=True, max_length=200, null=True)),
                ('expires_in', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
