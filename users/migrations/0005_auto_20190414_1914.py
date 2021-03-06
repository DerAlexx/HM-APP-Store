# Generated by Django 2.1.7 on 2019-04-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190414_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='fb',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='github',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='insta',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='linkedin',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='twitter',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='website',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='xing',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='youtube',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
    ]
