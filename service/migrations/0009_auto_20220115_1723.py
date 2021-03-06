# Generated by Django 3.2.9 on 2022-01-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_alter_post_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(default='media/', null=True, upload_to='media')),
            ],
            options={
                'verbose_name': 'Название',
                'verbose_name_plural': 'Иконка',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
