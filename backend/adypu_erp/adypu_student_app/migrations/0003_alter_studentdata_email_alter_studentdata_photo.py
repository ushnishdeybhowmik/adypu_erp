# Generated by Django 4.2.5 on 2023-10-03 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adypu_student_app', '0002_alter_studentdata_aadhar_card_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='Email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='Photo',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
