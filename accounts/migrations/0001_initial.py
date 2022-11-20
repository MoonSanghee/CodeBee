# Generated by Django 3.2.13 on 2022-11-19 22:38

import accounts.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone', models.IntegerField()),
                ('auth_number', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(error_messages={'unique': '같은 아이디가 이미 존재합니다.'}, max_length=16, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='아이디')),
                ('fullname', models.CharField(blank=True, max_length=20, null=True)),
                ('nickname', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='이메일 주소')),
                ('phone', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11), accounts.models.input_only_number])),
                ('profile_picture', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('address', models.CharField(max_length=100)),
                ('detail_address', models.CharField(max_length=30)),
                ('is_social_account', models.BooleanField(default=False)),
                ('git_username', models.CharField(blank=True, max_length=50, null=True)),
                ('boj_username', models.CharField(blank=True, max_length=50, null=True)),
                ('service_name', models.CharField(max_length=20, null=True)),
                ('social_id', models.CharField(blank=True, max_length=100, null=True)),
                ('social_profile_picture', models.CharField(blank=True, max_length=150, null=True)),
                ('is_phone_active', models.BooleanField(default=False)),
                ('is_email_active', models.BooleanField(default=False)),
                ('token', models.CharField(blank=True, max_length=150, null=True)),
                ('dislikes', models.ManyToManyField(related_name='ds', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('likes', models.ManyToManyField(related_name='ls', to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]