# Generated by Django 3.2.3 on 2022-08-05 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinclone', '0004_alter_gallery_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=122, null=True),
        ),
    ]
