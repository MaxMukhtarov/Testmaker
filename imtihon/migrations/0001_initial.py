# Generated by Django 4.1.6 on 2023-02-09 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('theme', models.CharField(max_length=255)),
                ('question_text', models.CharField(max_length=255)),
                ('choices', models.TextField()),
                ('right_choice', models.CharField(max_length=255)),
            ],
        ),
    ]
