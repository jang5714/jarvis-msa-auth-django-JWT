# Generated by Django 3.2.5 on 2021-12-24 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('body', models.TextField()),
                ('comment', models.TextField()),
                ('create_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('writen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'board',
            },
        ),
    ]
