# Generated by Django 4.2.16 on 2024-12-07 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0007_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dp',
            field=models.ImageField(blank=True, null=True, upload_to='user/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('A', 'Admin'), ('E', 'Employee'), ('C', 'Customer')], default='C', max_length=10),
        ),
    ]