# Generated by Django 3.1 on 2021-07-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_instagram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramHashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='Хештег')),
            ],
            options={
                'verbose_name': 'Хештег Instagram',
                'verbose_name_plural': 'Хештеги Instagram',
            },
        ),
    ]
