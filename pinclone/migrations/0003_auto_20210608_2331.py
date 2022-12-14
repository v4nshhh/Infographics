# Generated by Django 3.2.3 on 2021-06-08 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pinclone', '0002_profile_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='likes',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='pin_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin_comments', models.TextField(null=True)),
                ('pin_comment_created', models.DateField(auto_now_add=True)),
                ('pin', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='pinclone.gallery')),
                ('pin_comment_user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
