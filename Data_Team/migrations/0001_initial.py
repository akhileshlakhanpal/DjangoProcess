# Generated by Django 4.1.1 on 2022-09-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataT_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectcode', models.CharField(max_length=100)),
                ('question_label', models.CharField(max_length=100)),
                ('option_ans', models.CharField(max_length=100)),
            ],
        ),
    ]
